# Hermes setup notes

Use these notes within [Getting started](../getting-started.md). They map the portable guidance to a selected Hermes installation. Check its version and actual profile paths before changing files; no existing Hermes deployment is updated by this document.

For new named profiles, [native distribution setup](hermes-distribution.md) installs the shared package and supports later in-place updates. Existing default or non-distribution profiles keep the loading path below until a deliberate migration. [Deploy Harness](../../skills/deploy-harness/SKILL.md) coordinates the accepted shared and private sources for either path.

## Choose and configure the destination

1. Identify the intended profile and working project. Inspect their instructions, skills and retained state. Use an existing suitable profile or create one through the installed runtime's supported profile controls.
2. Reconcile the accepted OODA SOUL with `<profile-home>/SOUL.md`, preserving local personalisation and a backup. Replace `<profile-home>` with the selected Hermes home. Record its source revision and any installed adaptation. Keep repository contribution rules in their project scope.
3. Supply the complete selected skill folders through the profile's local `skills/` directory or supported external skill route. Preserve dependencies and check outbound references to the accepted source. Resolve name collisions before relying on the selected method.

Hermes's [file map](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what) distinguishes the profile SOUL, compact USER memory and project context. Its [skills guidance](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) describes local/external directories and discovery. External directories can be writable: record where adaptations or later skill edits occur rather than assuming a shared source is immutable.

## Profiles, projects and conversations

A Hermes profile supplies persistent configuration, memory, source connections and writable state. It can serve several roles. The sovereign individual is the human it serves; personal profile names and role archetypes are distinct from the reusable functions `interface`, `participant-a` and `participant-b`.

| Context | What it holds |
| --- | --- |
| Profile | General identity, model defaults, tools, memory and state. |
| Project | A workspace and its role/task instruction routes. |
| Ordinary chat, including a Master chat | Its own conversation history and selected model. |
| Group participant | A separate continuing conversation for that profile in that room. |

An interface profile can host several Master chats and participate separately in several role groups. Sharing a profile does not merge those histories. Group members need their own relevant role basis and retrieved context, as described [below](#interface-and-two-reusable-participants).

A model selected in a Master chat does not itself change the group's participants. Profile defaults, a chat's selected model and an existing room session's effective runtime can differ. Scope changes to the commissioned targets and verify their effective model and provider. Use the owning gateway's supported session model-switch or reset controls when an existing session retains an earlier route. Keep personal model preferences in the private deployment record.

## Profile identity and renames

Use the installed Hermes version's supported rename controls and read back the result. Renaming the built-in `default` profile changes its display name; renaming a named profile changes its canonical name and home. Check the [official profile guidance](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#managing-profiles) for that version. The profile names used below are examples.

Preserve chats, accepted role and source selections, model choices and credentials. Reconcile affected stored paths, project and group targets and connector permissions or identity guards. Keep a recoverable before-copy and retain dated records as history. Use supported identity-migration recovery where needed, then verify actual participant resolution rather than inferring it from command success.

Check the controls available for the actual room type. A profile rename does not guarantee that an existing room can rebind its members. When a replacement is commissioned, preserve the old history, carry the accepted role basis and continuation forward, and update the Master and reader routes. Record the outcome and any unresolved choice with the existing private deployment owner.

## Connect personal context and begin work

Use the selected profile's `memories/USER.md` for compact personal essentials and the route to the fuller private bundle. Preserve its existing entries and keep credentials separate. Finish configuration with [profile connection](../getting-started.md#finish-installation-connect-your-private-profile), then start a new session so it receives the changed SOUL, USER and project context. Follow [first use](../getting-started.md#begin-useful-authorised-work).

Check the selected identity, project context, skill discovery and actual reference/profile access. If different instructions take precedence or a path is missing, repair that route and report the remaining gap. A file in the working directory alone does not establish identity loading.

## Connect working sources and chat history

Follow [Connection assembly](../connections.md) for application OAuth and cross-runtime chat visibility. Keep the source reader, secure connection and permission scope distinct. Prefer native and official options, then suitable community components, and verify the actual consuming profile. A broad recent-chat catalog can support orientation while transcript reads remain selective and permission-based.

Record profile-specific connection results and updates with the existing private deployment owner. A working Codex connector is not evidence of Hermes access, and one profile's OAuth does not connect the other two. Do not add every available tool during package installation or claim two-way access from a one-direction test.

## Bind a working project to its role

Use [Check role bindings](../getting-started.md#check-role-bindings) when setting up a commissioned role project or refreshing one. Inspect the installed Hermes version and its supported project instruction mechanism. Save a compact route to the selected shared role, private sleeve, brief and work records in that project scope. Keep IDEA.md as the project description and the profile SOUL as its general identity. Verify that a new or supported refreshed project chat receives the instructions; reading the role manually in an existing chat proves retrieval only.

A native group is a separate working context. Its bots do not inherit the role from a project chat merely because they represent the same profiles. Reconcile existing rooms or commission a new one through [group bootstrap](../bootstrap-group.md), preserving its continuation and each member's complete relevant basis.

## Set up an eval group

Start from the role's private group Markdown. Copy the [Hermes Bots Group Settings Template](../eval-group-template.md) for a new group. Fill in the actual settings and link the completed file from the role's sleeve.

Use the [evaluation guide](../evaluating-role-groups.md) to decide when a role's Master would benefit from a group review.

To reproduce the three-bot setup, prepare **three distinct Hermes profiles** on the intended connection. Reuse suitable existing profiles, including the default profile, and create any missing ones from the Bots roster. Follow the [profile setup and private connection](#connect-personal-context-and-begin-work) for each profile and verify its source access. [Hermes Bot Mode](https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode) describes the roster and room controls.

| Room member | Responsibility |
| --- | --- |
| Harness reviewer | Represents the harness. Checks that the group applies the selected role contract, steering, evidence and relevant lived experience. Can also act as routing lead. |
| Peer A | Takes one vantage point for the eval. For a relational eval, this can be the sovereign’s position. |
| Peer B | Takes the complementary vantage point. For a relational eval, this can be the counterpart’s position. |

Assign the peers’ vantage points for each case. In reciprocal work they can exchange giver and active receiver. The Master is the separate project conversation that commissions the work, integrates the return and owns the recommendation. It can run under the reviewer’s profile.

1. Create or find the room on the intended Hermes connection. Seat the reviewer and both peers for the three-bot setup and verify the actual member profiles. Set **Purpose**, **Shared notes** and reply routing from the completed template.
2. Follow [Bootstrap a role group](../bootstrap-group.md) to connect the room participants to the selected shared role definition, private application and current work. In the existing private deployment or role record, keep the Master workspace, owning connection, room ID, members and their functions, selected revisions, and dispatch and return route. If the room changes, update the binding and verify the new route before using it.
3. From the Master, send one real review question with the artifact or decision, evidence, vantage points and expected return. Verify that the intended participants receive it, can open the relevant sources and return findings the Master can use. Keep the result with the existing case owner.

## Assemble a role deliberately

Follow the [role assembly path](../../roles/ROLE-TEMPLATE.md#assemble-this-role). [Profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles) distinguish persistent state from a running agent and warn against two processes writing the same profile home. Give both participants the relevant accepted basis while defining their state and write ownership explicitly.

Hermes [delegation](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation) supplies temporary-worker mechanisms, including steering. A fresh child and its returned summary do not alone establish the continuing reciprocal role. Check the selected mechanisms for exchange, context and recovery before claiming paired operation.

## Interface and two reusable participants

**Implementation candidate:** this maps the [shared paired-role design](../ecology-of-mind.md#the-atomic-operating-unit) to native Hermes groups. It does not replace the manual-session option below. End-to-end bootstrap, loading and useful room operation still require deployment-specific verification.

For a short reusable commissioning entry, use [Bootstrap a role group](../bootstrap-group.md). The mapping below supplies the Hermes-specific profile, room and loading boundaries. The selected role contract and current assignment govern the work. Use [Evaluate a role group](../evaluating-role-groups.md) to review the resulting work and its whole effort.

For a single outward interface and reusable peers, use the following profile functions:

| Function | Example profile | Scope |
| --- | --- | --- |
| `interface` | Existing default profile, displayed as Sovereign [your name] | Carry the user's intent, relevant context and decisions into the discussion; integrate a coherent response while preserving material disagreement. |
| `participant-a` | `agents-a` | Independent participant A, adopting the role assigned by the current room. |
| `participant-b` | `agents-b` | Independent participant B, adopting the same role from the same relevant basis. |

The same complete accepted foundation serves all three. A/B each receive the selected shared role definition, private application, purpose, relevant system-wide units of account and current brief. They retain complete OODAs and complementary positions that can reverse; neither is permanently the doer or final-only critic. The interface is an outward coordination function, not a substitute for either Twin or a new approval gate.

This is one useful topology, not a three-profile limit. Add other profiles when commissioned work needs them. Private sleeves specialise roles rather than duplicating the same application for every profile. Each participating context retrieves the relevant sleeve while retaining independent writable state.

1. **Map actual identities.** Reuse suitable existing profiles and create only missing ones through supported Hermes controls when authorised. Verify profile homes and intended model/capability access. Record the actual profile-to-function mapping in the existing private deployment binding or its linked receipt; no particular configuration filename or native Hermes field is implied. Do not infer ownership from the display name. Give each profile independent writable memory and state; readable shared source snapshots can be reused.

2. **Bootstrap each named target.** Use [Bootstrap](../bootstrap.md) and the installation steps above for all three profiles. Keep the shared SOUL general, with a short recorded function-specific adaptation. Individual role contracts belong in their assigned contexts, so A/B can serve several roles. Profile-wide memory/configuration remains shared across that profile's rooms; separate room conversations do not create hard memory or filesystem isolation. Reuse a working provider setup rather than changing it merely for installation.

3. **Keep setup work recognisable.** A Harness Engineering project in each profile can hold that profile's installation work. Optional working-folder names are `harness-engineering`, `harness-engineering-a` and `harness-engineering-b` under a chosen host workspace parent. Inspect actual paths and preserve existing bindings. A project's `IDEA.md` records its purpose and can be edited after creation; it is not the profile SOUL, an installation command or evidence of startup loading. A short description is: “Maintain this profile's accepted harness installation, source and private-context connections; verify loading and role-group participation, preserving local corrections, recovery information and unresolved issues.” Setup projects organise work; they do not instantiate extra role agents.

4. **Use one native room per commissioned role.** Create or reuse the intended group containing all three bots. Supply the selected whole role basis and current steering to each actual member context. In native [Bot Mode](https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode), a bot represents a profile and keeps its own continuing room session. Existing project chats do not automatically become those participants. Recover relevant prior decisions from their original sources; a room member is not automatically aware of every conversation in its profile. Verify supported instruction loading and available retrieval tools on the installed version. Do not directly resume hidden room sessions to bypass their driver.

5. **Exercise access and collaboration separately.** First verify the actual profile, project and folder. A sidebar that temporarily retains another profile's list is not evidence of chat access; let loading settle and check ownership. For a bounded history test, put a different harmless fact in a separate A/B setup chat, then ask each room member to retrieve its own fact with a source reference without putting the answers in the room prompt. Check against originals. Treat reading, prompting another chat and writing back as distinct capabilities. Then perform one useful bounded role assignment with consequential A/B exchange, an appropriate complementary reversal, a coherent user-facing result and a follow-up that recovers the same room contexts. Record unresolved gaps rather than inferring operation from three greetings.

Installation can finish before role commissioning. Do not create rooms or start role work solely to fill a configuration receipt. Shared guidance describes the intended relationship; actual speaking, routing, interruption and continuation depend on supported runtime controls and observed use. Keep exact identities, sources, adaptations and results in private installation/work records. Use native evidence before adding a telemetry collector or custom relay.

### Commission work selectively

Apply the [common working-arrangement rules](../operating-contract.md#choose-the-working-arrangement); a configured group is available capability, not a requirement to invoke every participant on every turn.

Use the Master chat for direct collaboration with the sovereign and routine work within the accepted brief. Commission the role group when its complementary perspectives could materially improve understanding, a consequential choice or the result. Supply a focused assignment with the relevant current material, outcome, scope and return condition, then integrate its useful findings into one response.

Once commissioned, both role participants exchange material contributions while they can still change the work, following the [common operating contract](../operating-contract.md#one-role-two-oodas). Match participation to the assignment rather than a fixed turn count. Judge group use by its useful contribution and whole effort, including tokens, latency and human supervision.

## Create the participant contexts

For a commissioned manual pair, use two separate profile homes and sessions. For new profiles, the supported profile commands are:

```sh
hermes profile create role-a
hermes profile create role-b
```

These are example names; choose unused names or inspect suitable existing profiles instead. For each new profile, configure provider/model access before applying the OODA files:

```sh
hermes -p role-a setup
hermes -p role-b setup
```

Select and verify the intended model and relevant tools/access for each participant. A suitable existing profile needs inspection rather than unnecessary setup. Then configure each through the steps above, using the same relevant model, capabilities and accepted OODA basis. Preserve independent writable state and finish each configuration with the private-profile connection step. Launch each in its own terminal, in the relevant project directory:

```sh
hermes -p role-a chat
hermes -p role-b chat
```

Supply both with the same [assignment and source routes](../operating-contract.md#bounded-assignment), individual contract, common contract, applicable methods and relevant private context. Identify the actual participants and their initial polarities in the existing private record. Have both retrieve the governing basis.

Before paired work begins, initialise or reuse their assignment record and verify that both can retrieve it. Use supported, authorised messaging, or an operator/existing coordinator to transfer labelled contributions between the sessions as described in [role assembly step 5](../../roles/ROLE-TEMPLATE.md#assemble-this-role). Preserve the checkpoint so replacement sessions can recover both perspectives. If the selected surface cannot provide that exchange, record the missing connection and leave paired operation pending. This recipe has not been exercised as a role run.

Use the shared [update](../getting-started.md#update-an-existing-installation) and [recovery](../getting-started.md#recover-a-working-installation) paths. Updating Hermes itself and updating the OODA package are separate changes.

Official sources checked 24 October 2026; documented mechanisms are not evidence that this installation uses them. Current-package deployment, independent installation and useful paired operation remain to be demonstrated.

