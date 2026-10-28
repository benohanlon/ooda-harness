# Getting started

Use this assembly path to install the shared guidance, put it into use, or update an existing installation. A human or an agent can follow it. The result should be a known revision, working instruction and skill routes, a small private working home where chosen, a resolved private-profile connection and a recoverable next assignment.

**Private alpha:** this is a manual guide, not a one-click installer or evidence of independent installation. Creating an enduring role follows the [role assembly path](../roles/ROLE-TEMPLATE.md#assemble-this-role); installing the package alone does not start its participants.

## Choose your path

- **First installation:** follow the steps below, using the [Codex](runtimes/codex.md) or [Hermes](runtimes/hermes.md) notes for the selected runtime.
- **Update, reinstall or refresh:** begin with [Update an existing installation](#update-an-existing-installation).
- **Something no longer works:** use [Recover a working installation](#recover-a-working-installation).
- **The harness is configured and you need a role:** use the [role template](../roles/ROLE-TEMPLATE.md#assemble-this-role).

## Establish the destination and preserve existing work

Identify the user, machine or execution host, runtime/version and project or profile receiving the installation. Check its current instructions, skills and private-profile choice before making changes. Recover existing answers and permissions; ask only for gaps that change the setup.

Keep a short installation record in the user's chosen private configuration or existing deployment record. Record the accepted source revision and location, files this installation manages, runtime loading routes, relevant dependencies, private bindings and previous working revision. Back up files before replacing them. Preserve unrelated instructions, skills and later local corrections.

**Expected result:** the destination and managed files are known, and existing work can be restored. Resolve an uncertain destination before writing there. Missing optional service connections can wait until an assignment needs them.

## Supply the accepted package

Choose an accepted Git revision and keep its files together. Use authorised repository access; a private repository needs access before it can be obtained. With Git, clone into a new destination and select the agreed commit:

```sh
git clone https://github.com/benohanlon/ooda-harness.git ooda-harness
git -C ooda-harness checkout --detach ACCEPTED_COMMIT
git -C ooda-harness rev-parse HEAD
```

Replace `ACCEPTED_COMMIT` with the agreed full commit SHA. If `ooda-harness` already exists, choose a different destination and use that name in all three commands. An existing installation follows the update path instead of resetting its working files. An authorised snapshot download is also suitable if its revision is recorded and checked.

Start with [README](../README.md), [SOUL](../SOUL.md) and [AGENTS](../AGENTS.md). The repository's AGENTS routes contribution and role work; the runtime's startup guidance supplies the relevant shared defaults. Follow relative routes to the methods and references relevant to the assignment. A skill's `SKILL.md` does not include its linked references automatically.

**Expected result:** the supplied revision matches the accepted commit, and required files and references are accessible. Report a missing required file; do not substitute an older or guessed version silently.

## Configure instruction and skill loading

Follow the [Codex](runtimes/codex.md) or [Hermes](runtimes/hermes.md) notes. Use the selected runtime's supported mechanisms and check the installed version. Record where startup instructions and complete skill packages are loaded. Preserve personalisation, specialist procedures and project guidance.

The setup owner records the actual working folder and its startup, profile and project routes to the accepted shared and private sources. The working folder can sit outside those snapshots. Reuse working bindings and configure missing routes explicitly; matching filenames and readable links do not establish loading. Verify actual loading in a fresh context using that folder, for both participants when a role pair is commissioned. Keep exact paths, revisions and verification evidence in the private installation record.

Keep the accepted source intact. If installed skill copies move away from their original directory, check links that leave those packages and adapt the installed routes to the accepted source. Record those adaptations so a later refresh can preserve them. A visible skill name establishes discovery; inspect method and reference access when the work uses them.

**Expected result:** the intended runtime can find its shared guidance, selected skill packages and their dependencies. If an override, duplicate skill or moved reference selects different content, reconcile that route before relying on it. A repository update does not update an installation automatically.

## Create or connect your private harness

For personalised use, connect the shared package to a private working home you maintain. The [shared/private explanation](../README.md#shared-and-private-harnesses) defines that arrangement and meaningful sovereign sleeves. Reuse an existing private repository, folder or chosen store and its maintained owners. A profile bundle can be the starting home; it need not contain every connected project or record.

Use `ooda-harness` for the shared harness and `sovereign-<individual>-harness` for its private application. The generic example is `sovereign-individual-harness`; replace `individual` with the person's chosen identifier, for example `sovereign-alex-harness`. A display name can be **Sovereign Alex Harness**. These names identify the harnesses; they require neither GitHub storage nor a new repository or directory for each role. For an existing installation, preserve working addresses until an authorised migration reconciles its [active routes and bindings](#update-an-existing-installation).

1. **Recover the existing arrangement.** Inspect its entrypoint, chosen roles, private bindings and relevant records. Retain working locations and access boundaries. Resolve an unknown profile location through the final connection step below rather than asking twice. An explicit choice to continue with limited personal context remains valid.
2. **Make a small map.** Use the private README as the human-readable map: whom the harness serves, the selected shared revision, chosen team and routes needed for its first useful work. Add or reuse a short private `AGENTS.md` for agent orientation and routing, following the [private-home template](private-harness-template.md#private-agents-orient-an-arriving-agent). Keep shared contribution rules at their shared owner. Keep `sovereign.md` as the canonical personal portrait when that convention is used. Reuse the installation record for loading routes, managed adaptations and recovery; the setup owner must explicitly configure and verify runtime loading. Matching filenames alone do not establish inheritance.
3. **Connect any commissioned role.** If no role is commissioned, leave this connection pending. Otherwise, connect its selected shared definition and revision to its private application and relevant system-wide units of account. Where no shared role definition exists, use the shared template and common contract as its basis. Keep the customised contract at its private owner and connect the relevant working relationship, knowledge, memory, experience, briefs and later corrections. Record deliberate adaptations. Supply both participants with this [whole governing basis](ecology-of-mind.md#combined-role-basis) during commissioned [role assembly](../roles/ROLE-TEMPLATE.md#assemble-this-role). Independent projects retain their assets, permissions and lifecycle. This step alone does not create or start participants.
4. **Retain experience where it is useful.** Use existing task, case and project records. When a case merits future reuse, add a concise route from the role's knowledge map or existing index. Retain its task/method and source revision, consequential choices and corrections, observed or pending outcome, failures/limitations, permission and future retrieval cue. A curated index can point to originals without copying them. Keep personal lessons with their private owners; propose permitted portable lessons at the relevant shared definition or method, and capability gaps at their implementation owner. Follow the [existing learning rules](operating-contract.md#correction-review-and-learning). Do not promote every assignment or load the whole archive.

For example, an existing `README.md` can route to `sovereign.md`, a first private role contract and its current work. Add a separate experience index only when useful cases warrant it. Keep runtime identifiers and access bindings in private configuration, and credentials outside tracked content. No fixed directory tree, separate repository per sleeve or new memory service is required.

**Expected result:** the private entrypoint records the personal-context choice and accepted shared basis, plus the private application, shared axis and relevant project and experience owners for any commissioned role. Verify the routes and applicable access. A role or its participants can remain uncommissioned while installation finishes. Missing optional detail can develop during useful work. Finish configuration with the profile-connection procedure below, preserving its resolved choice.

## Supply private personal context

Reuse a supplied private profile. If the user chooses to create one, adapt the [Sovereign Profile template](sovereign-profile-template.md) in a chosen private home outside the reusable package. Put established personal answers and communication preferences directly in that profile or its internally linked detail. Give the working context access to the relevant files. A choice to continue without a profile is resolved in the connection step below. Ordinary profile use should not require access to the creator's Notion workspace.

Keep credentials outside the profile. Exact submitted documents, correspondence and changing case facts remain with their case owners. Supply those inputs when an assignment needs them, with applicable authority and the current checkpoint. An external service is optional until the work depends on its live records.

## Finish installation: connect your private profile

Make this the final configuration step on every installation, reinstallation or refresh. Check the connection for the selected user and runtime, preserving it through shared-package updates.

1. **Reuse a known connection.** Read the existing private configuration or setup record, then open the profile entrypoint and relevant internal files. Preserve its location and personal content. If it works, report that it was retained without asking again. Use a supplied location; do not guess from an account name or default to the creator's profile.
2. **Ask when needed.** If the location is unknown, ask: "Where is your Sovereign Profile, for example sovereign.md? You can connect an existing file or private repository, create a small profile, or continue without one." If a known location is inaccessible, retain it, explain the access problem and ask for the missing access or an alternative.
3. **Save the choice privately.** Record the source location, entrypoint and runtime loading route in the existing installation configuration or setup record, outside the shared package. Preserve an explicit choice to continue without a profile on refresh. Revisit it only when the user requests setup or an assignment needs missing personal context.
4. **Connect subsequent sessions.** Configure supported startup guidance to supply compact essentials and instruct retrieval of relevant detail. Verify the saved route and actual access before reporting it connected. If unresolved, report the connection as pending and continue work supported by the available context.

For [Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what), use the selected profile's native `USER.md` for compact essentials and the private route. For [Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md), preserve existing user guidance and add the route to the applicable user-level `AGENTS.md`. The fuller bundle stays outside the startup summary. These instructions do not implement an automated installer.

## Begin useful authorised work

After finishing configuration with the profile step above, start or refresh the affected runtime context. Confirm the active instruction route and accepted revision, then have the agent open the required method/reference and relevant private detail for a real assignment. Reading a file on request demonstrates access; distinguish that from observing startup loading or correct application.

Give the agent a concrete outcome, relevant sources, authority and destination. Existing [Perception Check](../skills/perception-check/SKILL.md) guidance can help establish what needs attention, using sources actually available. Partial context is compatible with useful work; report a material gap and continue unaffected work.

When an enduring role is commissioned, use the [role assembly path](../roles/ROLE-TEMPLATE.md#assemble-this-role) to supply its individual contract, the [common operating contract](operating-contract.md), current brief and two actual participating contexts. Temporary workers do not become enduring roles.

Apply proportionate review to the actual result and inspect saved changes when saving is part of the assignment. Keep what was prepared, accepted, installed and observed distinct. Retain decisions and the next useful action in the existing work record so the assignment can continue.

**Expected result:** a useful bounded result and a continuation record, with installation, loading, access, execution and usefulness reported separately. If only configuration was commissioned, report the verified configuration and leave useful execution pending; do not start another assignment to fill the gap.

## Update an existing installation

Use this path for shared-package changes, reinstalls and refreshes. A private-profile revision or a runtime upgrade is a separate change: identify which source or configuration is changing.

1. **Recover the current installation record.** Identify its accepted revision, managed files, active contexts and profile connection. Compare current files with that record to find later local edits. Preserve uncertain or newer work before replacing anything.
2. **Stage the selected revision separately.** Read the relevant changes, keep complete packages together and check affected references and runtime compatibility. Reconcile local customisation with the new source. Return a material unresolved choice to its owner while continuing independent preparation.
3. **Activate the reconciled change.** Back up the affected managed files and configuration, then replace only the agreed scope. Record the new source revision, installed adaptations and previous working state. Preserve the [private-home map and sleeve connections](#create-or-connect-your-private-harness), unrelated skills, permissions, project records and private experience.
4. **Finish configuration with the [private-profile connection step](#finish-installation-connect-your-private-profile).** Retain a working connection or an explicit choice to continue without one. Reconcile local profile corrections with its private canonical source before refreshing that bundle.
5. **Verify the affected surface.** Refresh the relevant context and check its active routes, references and required access. Use the next authorised work to assess changed behaviour; repeat a broader runtime check only where the change warrants it. Record exact completed and pending items, including the state of existing role participants.

**Expected result:** the changed installation is identified and checked, personalisation is preserved, and recovery remains possible. An older session may still contain earlier instructions; updating files alone is not proof that it refreshed.

## Recover a working installation

Locate the last working record and backups. Compare active files and records first, preserving later decisions and private work. Restore only the affected managed files, source routes and configuration. Keep a source snapshot while any active route still references it.

Finish configuration with the [private-profile connection step](#finish-installation-connect-your-private-profile), then refresh the affected context and recheck relevant loading and access. Record what was restored and what remains unresolved. For a running role, follow [checkpoint and restoration](operating-contract.md#work-checkpoints-and-restoration), including uncertain external effects before retrying.

## Basis

This path applies the harness's existing version, private-context and recovery boundaries. Its goal-led sequence and expected results draw on [Diátaxis](https://diataxis.fr/how-to-guides/), [Google's procedure guidance](https://developers.google.com/style/procedures) and [HSE's user/task-centred guidance](https://www.hse.gov.uk/humanfactors/topics/procedures.htm). Runtime notes cite their own official sources. These references inform guide design; they do not establish operational performance of this harness.

[Profile template](sovereign-profile-template.md) · [Roles](../ROLES.md) · [Skills](../SKILLS.md) · [README](../README.md)
