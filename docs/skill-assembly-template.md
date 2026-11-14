# Assemble an OODA skill

A skill gives an agent a reusable way to produce an outcome. Start with the decision or work someone needs, who benefits, and the evidence that would show a useful result. Use the current assignment and role contract to supply authority and accountability.

## Package the method

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

## Bind and verify in the runtime

Pin the accepted skill source and dependencies in the existing private deployment record. For Hermes, use the profile's supported skill location, such as the profile-local skills directory or `skills.external_dirs`. Record the profile and project, selected copy, and relevant connections, tool permissions and plugin routes. Use the [Hermes runtime guide](runtimes/hermes.md) and [connection assembly](connections.md). Prefer capabilities already supplied by the runtime. Add a plugin when it performs a job the skill actually needs.

Check discovery and the exact loaded revision in a fresh context, then verify the references can be read and required capabilities can do the work within scope. Run a representative request and inspect its output. Where a missing capability can change the result, check that case too. Across runtimes, compare the quality of the decisions, evidence and handoff under the same assignment. Record differences in access or observed behaviour. Use [runtime acceptance](operating-contract.md#runtime-acceptance) and the existing deployment record.

[Skill catalogue](../SKILLS.md) · [Agent Skills specification](https://agentskills.io/specification)
