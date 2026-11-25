"""Offline package checks and opt-in tests against Hermes's real installer.

Run with a Hermes Python environment and OODA_HERMES_SOURCE pointing to its
source checkout. Native tests create temporary homes and never create aliases,
contact providers, start gateways or modify an existing profile.
"""

import importlib
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

if os.environ.get("OODA_HERMES_SOURCE"):
    sys.path.insert(0, str(Path(os.environ["OODA_HERMES_SOURCE"]).resolve()))
    import hermes_yaml as yaml
else:
    import yaml


PACKAGE = Path(__file__).resolve().parents[1]
OWNED = {
    "distribution.yaml", "LICENSE", "SOUL.md", "README.md", "HARNESS-MAP.md", "AGENTS.md", "ROLES.md",
    "SKILLS.md", "LISTS.md", "docs", "roles", "skills", "lists", "examples",
    "assets", "brand",
}


class PackageBoundary(unittest.TestCase):
    def test_explicit_shared_payload(self):
        manifest = yaml.safe_load((PACKAGE / "distribution.yaml").read_text(encoding="utf-8"))
        self.assertEqual(set(manifest["distribution_owned"]), OWNED)
        self.assertTrue(all((PACKAGE / entry).exists() for entry in OWNED))
        self.assertNotIn("env_requires", manifest)
        # Recipient account settings, functions and private bindings are not shipped.
        for path in ("config.yaml", "mcp.json", "auth.json", "memories", "sessions", "ooda", "local"):
            self.assertNotIn(path, manifest["distribution_owned"])

    def test_no_private_files_inside_owned_directories(self):
        forbidden = {"auth.json", ".env", ".ssh", "mcp-tokens", "private", "memories", "sessions"}
        for root in OWNED:
            entry = PACKAGE / root
            if entry.is_dir():
                for path in entry.rglob("*"):
                    self.assertFalse(path.is_symlink(), str(path.relative_to(PACKAGE)))
                    self.assertNotIn(path.name.casefold(), forbidden, str(path.relative_to(PACKAGE)))


@unittest.skipUnless(os.environ.get("OODA_HERMES_SOURCE"), "set OODA_HERMES_SOURCE for native tests")
class NativeDistribution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scratch = tempfile.TemporaryDirectory(prefix="ooda-native-distribution-")
        cls.root = Path(cls.scratch.name).resolve()
        cls.home = cls.root / "hermes-home"
        cls.home.mkdir()
        cls.saved_env = {key: os.environ.get(key) for key in ("HERMES_HOME", "HERMES_CONFIG_BACKEND")}
        os.environ["HERMES_HOME"] = str(cls.home)
        os.environ["HERMES_CONFIG_BACKEND"] = "file"
        cls.native = importlib.import_module("hermes_cli.profile_distribution")
        profiles = importlib.import_module("hermes_cli.profiles")
        # Fail before any install if the runtime did not respect the isolated home.
        if profiles._get_default_hermes_home().resolve() != cls.home:
            raise RuntimeError("Hermes did not resolve the temporary test home")
        if profiles._get_profiles_root().resolve() != cls.home / "profiles":
            raise RuntimeError("Hermes did not resolve the temporary profiles root")

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.saved_env.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
        cls.scratch.cleanup()

    def fixture(self, name):
        destination = self.root / name
        shutil.copytree(PACKAGE, destination, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        # These synthetic strays must not enter a recipient profile.
        self.write(destination / ".env", "SYNTHETIC_SECRET=not-a-real-key\n")
        self.write(destination / "private" / "portrait.md", "synthetic private context")
        self.write(destination / "unlisted.txt", "not distribution-owned")
        return destination

    @staticmethod
    def write(path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_install_update_and_independent_state(self):
        source = self.fixture("payload")
        homes = {}
        preserved = {}
        names = ("trial-interface", "trial-a", "trial-b", "trial-extra")
        original_soul = (source / "SOUL.md").read_bytes()
        for name in names:
            plan = self.native.install_distribution(str(source), name=name, create_alias=False)
            target = plan.target_dir.resolve()
            self.assertEqual(target, self.home / "profiles" / name)
            self.assertEqual((target / "SOUL.md").read_bytes(), original_soul)
            self.assertTrue((target / "skills" / "deploy-harness" / "SKILL.md").is_file())
            self.assertTrue((target / "docs" / "bootstrap.md").is_file())
            for unshipped in (".env", "private", "unlisted.txt"):
                self.assertFalse((target / unshipped).exists(), unshipped)
            markers = {
                "config.yaml": "model: synthetic-local-choice\n",
                "mcp.json": '{"mcpServers": {}}',
                "auth.json": '{"synthetic": true}',
                ".env": "SYNTHETIC_KEY=local-placeholder\n",
                "memories/USER.md": f"Personal context for {name}",
                "sessions/synthetic.json": f'{{"profile": "{name}"}}',
                "local/function.md": f"Private function for {name}",
                "ooda/current.json": f'{{"private_pin": "synthetic-accepted-{name}"}}',
                "skills/local-example/SKILL.md": f"Local method for {name}",
            }
            for relative, value in markers.items():
                self.write(target / relative, value)
            homes[name] = target
            preserved[name] = {relative: (target / relative).read_bytes() for relative in markers}

        # A native update uses its recorded local source, not a replacement profile.
        self.write(source / "SOUL.md", original_soul.decode("utf-8") + "\nSynthetic update marker.\n")
        manifest = yaml.safe_load((source / "distribution.yaml").read_text(encoding="utf-8"))
        manifest["version"] = "0.1.0-test.2"
        self.write(source / "distribution.yaml", yaml.safe_dump(manifest, sort_keys=False))
        self.native.update_distribution("trial-a")
        self.assertEqual((homes["trial-a"] / "SOUL.md").read_bytes(), (source / "SOUL.md").read_bytes())
        for name in ("trial-interface", "trial-b", "trial-extra"):
            self.assertEqual((homes[name] / "SOUL.md").read_bytes(), original_soul)
            self.native.update_distribution(name)
        for name, target in homes.items():
            self.assertEqual((target / "SOUL.md").read_bytes(), (source / "SOUL.md").read_bytes())
            for relative, value in preserved[name].items():
                self.assertEqual((target / relative).read_bytes(), value, f"{name}: {relative}")
            installed = self.native.read_manifest(target)
            self.assertEqual(installed.version, "0.1.0-test.2")
            self.assertEqual(Path(installed.source).resolve(), source)
        # A second ordinary update remains usable without resetting personal state.
        self.native.update_distribution("trial-a")
        for relative, value in preserved["trial-a"].items():
            self.assertEqual((homes["trial-a"] / relative).read_bytes(), value)

    def test_refuses_default_and_existing_unmanaged_profile(self):
        source = self.fixture("refusal-payload")
        self.write(self.home / "SOUL.md", "Synthetic default profile")
        unmanaged = self.home / "profiles" / "trial-existing"
        self.write(unmanaged / "SOUL.md", "Synthetic existing profile")
        before = (unmanaged / "SOUL.md").read_bytes()
        with self.assertRaises(self.native.DistributionError):
            self.native.install_distribution(str(source), name="default", create_alias=False)
        with self.assertRaises(self.native.DistributionError):
            self.native.install_distribution(str(source), name="trial-existing", create_alias=False)
        with self.assertRaises(self.native.DistributionError):
            self.native.update_distribution("trial-existing")
        self.assertEqual((unmanaged / "SOUL.md").read_bytes(), before)
        self.assertEqual((self.home / "SOUL.md").read_text(encoding="utf-8"), "Synthetic default profile")


if __name__ == "__main__":
    unittest.main(verbosity=2)
