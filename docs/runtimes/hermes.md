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

## Create the participant contexts

For a commissioned manual pair, use two separate profile homes and sessions. For new profiles, the supported profile commands are:

```sh
hermes profile create role-a
hermes profile create role-b
```

These are example names; choose unused names or inspect suitable existing profiles instead. Configure each through the steps above, using the same relevant model, capabilities and accepted OODA basis. Preserve each profile's independent writable state and finish each configuration with the private-profile connection step. Then launch each in its own terminal, in the relevant project directory:

```sh
hermes -p role-a chat
hermes -p role-b chat
```

Supply both with the same [assignment and source routes](../operating-contract.md#bounded-assignment), individual contract, common contract, applicable methods and relevant private context. Identify the actual participants and their initial polarities in the existing private record. Have both retrieve the governing basis.

Before paired work begins, initialise or reuse their assignment record and verify that both can retrieve it. Use supported, authorised messaging, or an operator/existing coordinator to transfer labelled contributions between the sessions as described in [role assembly step 5](../../roles/ROLE-TEMPLATE.md#assemble-this-role). Preserve the checkpoint so replacement sessions can recover both perspectives. If the selected surface cannot provide that exchange, record the missing connection and leave paired operation pending. This recipe has not been exercised as a role run.

Use the shared [update](../getting-started.md#update-an-existing-installation) and [recovery](../getting-started.md#recover-a-working-installation) paths. Updating Hermes itself and updating the OODA package are separate changes.

Official sources checked 24 October 2026; documented mechanisms are not evidence that this installation uses them. Current-package deployment, independent installation and useful paired operation remain to be demonstrated.
