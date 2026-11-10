# Install and update the Hermes foundation

Use this guide within [Bootstrap](../bootstrap.md) and the [Hermes runtime mapping](hermes.md). The root `distribution.yaml` makes the shared repository a native Hermes profile distribution. It supplies reusable software, not the recipient's private harness or an operating role.

## What this package owns

The manifest explicitly names the shared SOUL, catalogues, guidance, role definitions, skills, examples and artwork. This keeps their relative references together. `AGENTS.md` retains its repository-contribution scope. Its presence in a profile does not make every user task a contribution to OODA Harness.

The distribution does not ship model/provider settings, MCP connections, cron jobs, credentials, user memories, chat history or private sleeves. It does not own `local/`, `memories/`, `sessions/`, the profile's private `ooda/` bindings or other runtime state. Keep per-user source connections and per-profile functions at their existing private owners. Do not place personal adaptations inside files the distribution updates.

Installation requires an existing Hermes runtime with native profile-distribution support and Git. Check the actual installed commands first. Updating Hermes itself is a separate operation. Use the [official guide](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions) and [command reference](https://hermes-agent.nousresearch.com/docs/reference/profile-commands) for the supported flags on that version.

## 1. Select the source and targets

Follow Bootstrap's source-access and destination checks before activation. Recover the actual profile home and its existing state on the execution host. A cloud Desktop connection does not put its backend on the local computer.

Targets are a user-selected list. A typical first setup uses `ooda-interface`, `ooda-a` and `ooda-b`, with additional profiles added when needed. Those are example names, not a fixed count, reserved role names or permission grants. Each receives the same shared foundation and its own writable state. Its private setup records whether it is an interface, participant or another commissioned function.

For a controlled first install, prepare a clean local Git checkout at the accepted full commit. Keep it outside the profile's user-data directories, with the origin, exact revision and private deployment record retained. The agent can use ordinary Git commands to fetch and select that revision. Preserve unrelated working changes and reuse a suitable existing checkout.

```bash
# Run in the chosen shared-source checkout after verifying source access.
git fetch origin
git checkout --detach <accepted-full-commit>
git status --porcelain
```

Check the actual commit and clean tracked source, including `distribution.yaml`, before continuing. Also inspect untracked and ignored files inside the manifest-owned paths. A local source is copied from the filesystem, so ignored credentials nested inside a skill can enter the payload on some Hermes versions. Use a clean checkout containing only the accepted source there. Do not rely on `.gitignore` or native exclusions to sanitise a working profile. Do not run these commands in the user's private repository or overwrite an unrelated working tree. The literal bracketed values in this guide require the user's accepted inputs.

Hermes currently tracks the default branch for a Git-URL distribution source. An advertised version or Git tag is not proof that the installer selected that tag. This is why the controlled bootstrap uses a verified checkout. Native Git-URL installation is available for an agreed moving release source, with that update policy explicit. Do not promise exact-ref installation until the installed Hermes version supports it.

## 2. Install the shared foundation

Run native installation for each commissioned new named profile. The chosen checkout is the native distribution source. For example:

```bash
hermes profile install /path/to/verified-ooda-checkout --name ooda-interface
hermes profile install /path/to/verified-ooda-checkout --name ooda-a
hermes profile install /path/to/verified-ooda-checkout --name ooda-b
```

Hermes records the source location for later updates. Keep that checkout available on the execution host. Native confirmation remains in place. No wrapper, profile export, custom profile copier or new runtime is required.

The built-in `default` profile cannot be a distribution target. Preserve an existing interface there through Bootstrap's established file-loading/update path. Existing named profiles without distribution metadata also remain on that path until their migration is commissioned and reviewed. `--force` can replace authored configuration and is not a routine conversion strategy.

For community use, recipients with access can also install this distribution directly from its Git repository. That follows the source's default branch. A public community release and licence remain deliberate publication decisions, separate from this private alpha implementation.

## 3. Connect the private half and verify use

Finish [the private-profile connection step](../getting-started.md#finish-installation-connect-your-private-profile) in each target. Recover its existing private binding first. In a fresh environment, ask for the recipient's own private location and authorised access, then save the binding privately. If none exists, use [Create or connect your private harness](../getting-started.md#create-or-connect-your-private-harness) to establish a minimal home, or record the user's explicit shared-only choice. Do not guess a repository from their username.

Reuse one authorised private source where suitable, with independently maintained profile bindings and state. Private sleeves specialise commissioned roles, not each runtime profile. Preserve each role's selected shared foundation. Configure only the model/provider and account connections required by the commission, through native setup.

Record the target's function privately and connect its retrieval through the profile's user-owned personal-context route, such as `memories/USER.md`. Do not append it to the distribution-owned SOUL and expect a native update to preserve that edit. The shared package does not contain the creator's private source URL or a fixed function assignment. A provider sign-in, connection in another profile or remembered group discussion does not establish loading or access in this target.

Start a fresh context, or use the runtime's supported refresh route, and verify the selected shared guidance, relevant private entry and actual source access. Complete useful commissioned work and inspect its result. Report installation, private connection, loading and execution separately. No model-backed turn is required merely to validate the distribution's file-copy behaviour.

## 4. Update deliberately

First inspect local edits in distribution-owned files and retain a recovery copy of the affected profile setup through the existing deployment owner. Compare the newly accepted shared source with the installed selection. Keep personal changes and functions in their user-owned destinations, and reconcile meaningful changes before overwriting shared files.

If the native source is a verified local checkout, fetch and select the newly accepted commit in that same clean checkout. Verify origin, revision and source access again. Then update only the commissioned distribution profiles:

```bash
hermes profile update ooda-interface
hermes profile update ooda-a
hermes profile update ooda-b
```

For a Git-URL source, native update fetches that recorded source's default branch. Keep the accepted-source policy explicit. Use `hermes profile info <name>` to inspect the recorded source and distribution version, and retain exact Git provenance in the private deployment receipt.

Normal native update preserves `config.yaml` and user data. This distribution ships no `mcp.json` or cron definitions. Shared SOUL, methods and references can change, so refresh and verify their actual consumers. Check the private connection and selected role references before calling the personalised update complete. Update additional profiles from the same target list as required, and record any partial failure rather than treating the batch as atomic.

When the commission includes a private refresh, fetch and reconcile that separately accepted source through its existing binding. Stage it in the private environment, preserve local corrections and deliberately update the private binding. It never enters this distribution. The same Deploy Harness method coordinates both sources without requiring a duplicate installer or a public copy of private sleeves.

Do not delete/recreate profiles or use `--force-config` as ordinary update behaviour. Recover through [the established recovery guide](../getting-started.md#recover-a-working-installation) when necessary. Native update is not a general rollback system and does not verify role-group cognition.

## 5. Commission role groups when needed

Use [Bootstrap a role group](../bootstrap-group.md) with the existing profiles, selected shared role, private sleeve, purpose and current brief. Select actual participants and connect the record and exchange routes. Each role uses its continuing contexts. Adding a profile or updating shared files does not commission every available role or import conversations from other projects.

The group guide remains the human/agent handoff. Automate repeated setup only after a supported native mechanism and an actual remaining need are established. Read [role-group evaluation](../evaluating-role-groups.md) when reviewing useful interaction.

## Implementation and evidence

The development file `tests/test_hermes_distribution.py` checks manifest ownership and invokes the installed native installer in an isolated Hermes home when explicitly supplied a Hermes source path. It exercises installation and update of synthetic profiles, including personal-state preservation and a fourth profile. It makes no provider calls or account connections. Static checks alone do not establish runtime behaviour. Keep the actual test revision, results and remaining live setup with the private deployment receipt.

From a development checkout, run `python tests/test_hermes_distribution.py` with PyYAML for the static checks. To include native checks, set `OODA_HERMES_SOURCE` to the installed Hermes source checkout and use that installation's Python environment. The test refuses to proceed unless Hermes resolves its temporary home and profiles root. This calls the real installer functions, not the CLI launcher or a model-backed conversation. Tests are development files and are not part of the installed profile payload.
