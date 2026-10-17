# ooda-harness
A human-led OODA framework for coordinating useful AI work across career, clients, research, editorial and personal operations.

## Current component

[SOUL.md](SOUL.md) defines the shared identity, interaction, writing and judgement of the AI collaborator.

The reviewed SOUL is versioned here. An earlier revision ([7f6117b](https://github.com/benohanlon/ooda-harness/commit/7f6117be607a74c808eac43c3ac12b08162e700a)) was installed and checked in Hermes Cloud. No runtime check is claimed for the current revision. Hermes uses the copy at `HERMES_HOME/SOUL.md`; repository storage alone does not activate it.

The full README and operating components remain under development.

## Versioning and releases

Keep filenames such as `SOUL.md`, `README.md` and `AGENTS.md` stable. Git commits identify exact revisions. A release tag identifies the complete repository snapshot at one commit; individual files do not need separate release numbers.

Use [Semantic Versioning](https://semver.org/) tags in the form `vMAJOR.MINOR.PATCH`. Use `0.y.z` and pre-release labels such as `v0.1.0-alpha.1` during initial development. After `1.0.0`, use patch releases for compatible fixes, minor releases for compatible additions and major releases for incompatible changes to documented operating contracts or interfaces. Keep published tags fixed.

Record the Notion draft revision, published Git commit/release and installed runtime revision separately. Before promotion, compare the approved file body with the published source and retain the commit reference. A release versions repository definitions; it does not certify runtime loading, external records or useful outcomes.
