# Hermes setup notes

Use these notes within [Getting started](../getting-started.md). They map the portable guidance to a selected Hermes installation. Check its version and actual profile paths before changing files; no existing Hermes deployment is updated by this document.

## Choose and configure the destination

1. Identify the intended profile and working project. Inspect their instructions, skills and retained state. Use an existing suitable profile or create one through the installed runtime's supported profile controls.
2. Reconcile the accepted OODA SOUL with `<profile-home>/SOUL.md`, preserving local personalisation and a backup. Replace `<profile-home>` with the selected Hermes home. Record its source revision and any installed adaptation. Keep repository contribution rules in their project scope.
3. Supply the complete selected skill folders through the profile's local `skills/` directory or supported external skill route. Preserve dependencies and check outbound references to the accepted source. Resolve name collisions before relying on the selected method.

Hermes's [file map](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what) distinguishes the profile SOUL, compact USER memory and project context. Its [skills guidance](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) describes local/external directories and discovery. External directories can be writable: record where adaptations or later skill edits occur rather than assuming a shared source is immutable.

## Connect personal context and begin work

Use the selected profile's `memories/USER.md` for compact personal essentials and the route to the fuller private bundle. Preserve its existing entries and keep credentials separate. Finish configuration with [profile connection](../getting-started.md#finish-installation-connect-your-private-profile), then start a new session so it receives the changed SOUL, USER and project context. Follow [first use](../getting-started.md#begin-useful-authorised-work).

Check the selected identity, project context, skill discovery and actual reference/profile access. If different instructions take precedence or a path is missing, repair that route and report the remaining gap. A file in the working directory alone does not establish identity loading.

## Assemble a role deliberately

Follow the [role assembly path](../../roles/ROLE-TEMPLATE.md#assemble-this-role). [Profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles) distinguish persistent state from a running agent and warn against two processes writing the same profile home. Give both participants the relevant accepted basis while defining their state and write ownership explicitly.

Hermes [delegation](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation) supplies temporary-worker mechanisms, including steering. A fresh child and its returned summary do not alone establish the continuing reciprocal role. Check the selected mechanisms for exchange, context and recovery before claiming paired operation.

## Interface and two reusable participants

**Implementation candidate:** this maps the shared paired-role design to native Hermes groups. It does not replace the manual-session option below. End-to-end bootstrap, loading and useful room operation still require deployment-specific verification.

For a single outward interface and reusable peers, use the following profile functions:

| Function | Example profile | Scope |
| --- | --- | --- |
| `interface` | Existing default profile, displayed as Sovereign [your name] | Carry the user's intent, relevant context and decisions into the discussion; integrate a coherent response while preserving material disagreement. |
| `participant-a` | `agents-a` | Independent participant A, adopting the role assigned by the current room. |
| `participant-b` | `agents-b` | Independent participant B, adopting the same role from the same relevant basis. |

The same complete accepted foundation serves all three. A/B each receive the selected shared role definition, private application, purpose, relevant system-wide units of account and current brief. They retain complete OODAs and complementary positions that can reverse; neither is permanently the doer or final-only critic. The interface is an outward coordination function, not a substitute for either Twin or a new approval gate.

1. **Map actual identities.** Reuse suitable existing profiles and create only missing ones through supported Hermes controls when authorised. Verify profile homes and intended model/capability access. Record the actual profile-to-function mapping in the existing private deployment binding or its linked receipt; no particular configuration filename or native Hermes field is implied. Do not infer ownership from the display name. Give each profile independent writable memory and state; readable shared source snapshots can be reused.

2. **Bootstrap each named target.** Use [Bootstrap](../bootstrap.md) and the installation steps above for all three profiles. Keep the shared SOUL general, with a short recorded function-specific adaptation. Individual role contracts belong in their assigned contexts, so A/B can serve several roles. Profile-wide memory/configuration remains shared across that profile's rooms; separate room conversations do not create hard memory or filesystem isolation. Reuse a working provider setup rather than changing it merely for installation.

3. **Keep setup work recognisable.** A Harness Engineering project in each profile can hold that profile's installation work. Optional working-folder names are `harness-engineering`, `harness-engineering-a` and `harness-engineering-b` under a chosen host workspace parent. Inspect actual paths and preserve existing bindings. A project's `IDEA.md` records its purpose and can be edited after creation; it is not the profile SOUL, an installation command or evidence of startup loading. A short description is: “Maintain this profile's accepted harness installation, source and private-context connections; verify loading and role-group participation, preserving local corrections, recovery information and unresolved issues.” Setup projects organise work; they do not instantiate extra role agents.

4. **Use one native room per commissioned role.** Create or reuse the intended group containing all three bots. Supply the selected whole role basis and current steering to each actual member context. In native [Bot Mode](https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode), a bot represents a profile and keeps its own continuing room session. Existing project chats do not automatically become those participants. Recover relevant prior decisions from their original sources; a room member is not automatically aware of every conversation in its profile. Verify supported instruction loading and available retrieval tools on the installed version. Do not directly resume hidden room sessions to bypass their driver.

5. **Exercise access and collaboration separately.** First verify the actual profile, project and folder. A sidebar that temporarily retains another profile's list is not evidence of chat access; let loading settle and check ownership. For a bounded history test, put a different harmless fact in a separate A/B setup chat, then ask each room member to retrieve its own fact with a source reference without putting the answers in the room prompt. Check against originals. Treat reading, prompting another chat and writing back as distinct capabilities. Then perform one useful bounded role assignment with consequential A/B exchange, an appropriate complementary reversal, a coherent user-facing result and a follow-up that recovers the same room contexts. Record unresolved gaps rather than inferring operation from three greetings.

Installation can finish before role commissioning. Do not create rooms or start role work solely to fill a configuration receipt. Shared guidance describes the intended relationship; actual speaking, routing, interruption and continuation depend on supported runtime controls and observed use. Keep exact identities, sources, adaptations and results in private installation/work records. Use native evidence before adding a telemetry collector or custom relay.

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
