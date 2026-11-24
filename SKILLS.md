# Skills

This is the catalogue of OODA Harness's reusable skills, including methods being prepared. Each packaged skill has one maintained definition in its own `SKILL.md`; a planned entry does not imply that its file or installation exists. The [role directory](ROLES.md) identifies the continuing responsibilities. Role contracts link to relevant skills; several roles can use the same method within their remit and the current assignment's authority.

| Skill | Purpose | Coordination | Status |
| --- | --- | --- | --- |
| [Deploy Harness](skills/deploy-harness/SKILL.md) | Install, refresh or recover the shared foundation and the recipient's private connection in selected profiles or workspaces. | Head of Harness Engineering maintains the method. The current commission selects targets and accepted sources. | Native Hermes package install/update exercised in isolated profiles. Personalised loading and useful execution require deployment-specific checks. |
| [Perception Check](skills/perception-check/SKILL.md) | Refresh situational awareness by establishing the horizon, accessible field of vision, actual observations, useful findings and material gaps. | Chief of Staff normally coordinates the wider picture; you can request a check directly. | MVP method prepared and exercised with an isolated fixture; live installation, source access and useful runtime behaviour remain unverified. |
| [Writing and Editing](skills/writing-and-editing/SKILL.md) | Draft, edit and review prose, including advisory replies, while preserving meaning, evidence, argument and voice. | Shared across roles; the producing role remains accountable. | Method published. Hermes installation, loading and live use remain unverified. |
| [Sense of Taste](skills/sense-of-taste/SKILL.md) | Judge bounded work against its brief, original evidence, wider purpose and standards. Preserve successful work and identify material gaps and useful possibilities. | Shared judgement method within an enduring role's pair; it can also serve an explicitly assigned review. | Packaged definition prepared for review and manual testing. Installation, loading and useful live execution remain unverified. |
| [Community Research](skills/community-research/SKILL.md) | Investigate what relevant communities say about a harness-engineering question, following substantive discussion to original evidence and implementations. | Shared across roles; Research Lead maintains the method and community routes with Engineering's technical input. | Packaged definition prepared for review and manual testing. Installation, access to particular communities and useful live execution remain unverified. |
| [Health Check](skills/health-check/SKILL.md) | Review harness coherence, drift, correction quality and consolidation after substantial exploration or change. | Engineering maintains the shared method; current assignments and change owners retain authority. | Method packaged for manual use; installation and useful runtime performance remain unverified. |

For example: “Run a Perception Check for the past 72 hours. What needs my attention?”

For a schedule-only review, ask “Check the schedule”. The bounded [Schedule Check method](skills/perception-check/SKILL.md#schedule-check) is part of Perception Check. Its live manual test remains pending.

The timeframe belongs to the request. This example sets no recurring schedule and assumes neither a previous check nor complete access to personal materials.

For the harness itself, ask: "Run a Health Check on our shared/private guidance and the changes since the last review." Perception/360 establishes what needs attention; Health Check examines whether the harness still works coherently and whether corrections or reviews improved it. Use it for a material reconvergence when exploration has opened several strands, without adding a full audit to every task.

Writing and Editing applies the maintained [Writing and Editorial Standards](skills/writing-and-editing/references/EDITORIAL-STANDARDS.md). [SOUL.md](SOUL.md) requires their use; [AGENTS.md](AGENTS.md#retrieve-guidance-for-the-work) routes repository work and [ROLES.md](ROLES.md#coordination-and-shared-skills) covers delegation. Sense of Taste supplies a separate judgement method; Writing and Editing remains independently usable. The [common operating contract](docs/operating-contract.md) defines the pair, not either skill.

[LISTS.md](LISTS.md) routes to the packaged community directory, selected research resources and existing editorial references. Load resources when the assignment calls for them. Required package references and cross-skill dependencies must be available in the actual deployment; a link alone does not load them.

## Assembly

A skill gives an agent a reusable way to produce an outcome. Start with the decision or work someone needs, who benefits, and the evidence that would show a useful result. Use the current assignment and role contract to supply authority and accountability.

### Package the method

```text
<skill-name>/
├── SKILL.md
├── references/   # Detailed guidance and source routes, when needed
├── examples/     # Representative cases, when useful
└── scripts/      # Repeatable operations or checks, when needed
```

Only `SKILL.md` is required. Give it YAML frontmatter with `name` and `description` so the runtime can discover it. Describe what it does and when it applies. Use the body to capture the following where they affect the work.

- **Purpose and axis.** State who gets what outcome and how to judge a useful result. Route to the governing role and the operator's measures where they matter.
- **Decisions and evidence.** For each materially different request, specify what the agent needs to decide, which maintained source or section answers it, and which capability to use. Distinguish authoritative guidance and evidence from worked examples. An example can demonstrate the method with one audience or tool.
- **Dependencies and partial work.** Identify the capability that each operation needs and what can still proceed if it is absent. Use references selectively. Keep account choices, private source links and approved materials in the operator's private application. Keep credentials in the runtime's supported secret store.
- **Authority and handoffs.** Identify the owner of the action and where decisions, results or exceptions go. The current assignment supplies authority for actions. Respect the existing owners of case records and reusable guidance.
- **Return and learning.** Say what the agent returns, how it checks the result, and where a consequential correction or lesson should be retained for the next relevant use.

### Bind and verify in the runtime

Pin the accepted skill source and dependencies in the existing private deployment record. For Hermes, use the profile's supported skill location, such as the profile-local skills directory or `skills.external_dirs`. Record the profile and project, selected copy, and relevant connections, tool permissions and plugin routes. Use the [Hermes runtime guide](docs/runtimes/hermes.md) and [connection assembly](docs/connections.md). Prefer capabilities already supplied by the runtime. Add a plugin when it performs a job the skill actually needs.

Check discovery and the exact loaded revision in a fresh context, then verify the references can be read and required capabilities can do the work within scope. Run a representative request and inspect its output. Where a missing capability can change the result, check that case too. Across runtimes, compare the quality of the decisions, evidence and handoff under the same assignment. Record differences in access or observed behaviour. Use [runtime acceptance](docs/operating-contract.md#runtime-acceptance) and the existing deployment record.

[Skill catalogue](#skills) · [Agent Skills specification](https://agentskills.io/specification)

## Loading and connections

The repository holds the versioned skill source. The selected runtime must discover and load that source through its supported skills route. A catalogue entry does not install a skill. See the [Hermes skills guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) for its loading conventions.

Private account connections and changing access state stay with the account owner's private setup and working records. Perception Check establishes what the current runtime can actually access and reports material gaps. This catalogue does not inventory every bundled or third-party skill in an installation.

[Return to the README](README.md)
