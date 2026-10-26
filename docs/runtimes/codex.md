# Codex setup notes

Use these notes within [Getting started](../getting-started.md). They describe a manual mapping of OODA guidance to Codex. Check the installed host and current official documentation; this page is not an installer or a claim of runtime acceptance.

## Connect shared startup guidance

1. Inspect the selected scope's existing guidance and overrides. For user-wide defaults, use `AGENTS.md` in the effective Codex home (normally `~/.codex`); for one project, use that project's instruction chain. Preserve the existing file and project-specific rules.
2. Add a short startup route to the accepted OODA source. Include its exact revision and location, an instruction to read SOUL at assignment startup, routes to the shared writing standard and task-relevant role/skill guidance, and a private profile binding. Keep detailed definitions in the supplied source.
3. Start a new affected context and inspect which guidance it receives. A higher-priority override or a context that has not refreshed can leave the old route active. Resolve the actual selection before claiming the update loaded.

Official [AGENTS discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md) describes Codex-home and project scope, overrides and size limits. The OODA repository's AGENTS governs contribution and assignment routing; copying it wholesale into user-wide defaults would also spread its repository-specific rules.

## Make complete skill packages available

Use a skill location supported by the installed host. Current [skill documentation](https://learn.chatgpt.com/docs/build-skills) lists `.agents/skills` in a project and `~/.agents/skills` for user scope. Inspect an existing managed installation before choosing or changing its route.

Install the selected folders with their references and other declared dependencies. Reconcile name collisions and check cross-package links after relocation, following [the shared loading step](../getting-started.md#configure-instruction-and-skill-loading). Preserve unrelated skills. Confirm discovery, then open the method and required reference during relevant work. [Codex customisation](https://learn.chatgpt.com/docs/customization/overview) distinguishes guidance, skills and service connections.

## Create the participant contexts

When a role pair is commissioned, open two new Codex tasks in the selected project or two CLI sessions in that working directory. Set the same relevant model and available capabilities. Record the actual task/session identities in the private assignment record.

Give each the same accepted [assignment and source routes](../operating-contract.md#bounded-assignment), individual contract, common contract, SOUL, applicable methods and relevant private context. Identify each participant and its initial polarity within that brief. Have both retrieve the governing material; do not rely on inherited instructions or a displayed role name.

Before paired work begins, connect the contexts and initialise or reuse their assignment record using [role assembly step 5](../../roles/ROLE-TEMPLATE.md#assemble-this-role). Verify that both can retrieve the record. The operator or an existing authorised coordinator can transfer contributions between the two tasks when direct messaging is unavailable. Preserve each contribution's source, recipient and disposition in the existing checkpoint. If neither route is available, record exchange as unconfigured and leave paired operation pending.

This is a manual setup recipe, not an automated launcher or a demonstrated role run. Continue with the commissioned assignment and [runtime acceptance](../operating-contract.md#runtime-acceptance).

## Keep scheduled workers separate

Apply the [common scheduling rule](../operating-contract.md#scheduled-work-and-private-bindings) to every role. A scheduled worker returns to its accountable role and maintained records while the sovereign's active conversation remains available.

Current [scheduled-task documentation](https://learn.chatgpt.com/docs/automations) distinguishes tasks that return to an existing chat from standalone/background runs. [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) move delegated work into separate contexts. These are distinct choices: spawning a subagent after a foreground chat receives a scheduled wake does not establish isolation of that wake.

Inspect the actual saved target before changing a schedule. Select an authorised background execution destination supported by the installed host, supply its role/source/record routes, and preserve cadence, prior decisions, existing permissions and paused states. Do not silently create replacement schedules or new user chats. If suitable targeting or result delivery is unavailable, retain the exact gap rather than claiming a prompt-only fix. Verify the scheduled route in ordinary use with an active human conversation and scoped browser/write targets; muting notifications alone is insufficient.

## Finish and use

Keep the profile bundle and its binding outside the shared package. Make [profile connection](../getting-started.md#finish-installation-connect-your-private-profile) the final configuration step, then follow [first use](../getting-started.md#begin-useful-authorised-work). Supply relevant routes explicitly to any commissioned participant; automatic inheritance is not assumed.

For updates and recovery, use the shared [update](../getting-started.md#update-an-existing-installation) and [recovery](../getting-started.md#recover-a-working-installation) paths with this installation's managed files. A completed setup does not create the role pair; continue through [role assembly](../../roles/ROLE-TEMPLATE.md#assemble-this-role) when commissioned.

Official sources checked 24 October 2026. Verify them again when an installed version or changed behaviour requires it. The independently installed path and paired-role usefulness remain to be demonstrated.
