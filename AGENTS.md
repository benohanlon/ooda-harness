# Repository contribution guidance

This repository is the private development home for OODA Harness. The README records the accepted design; detailed role contracts and runtime behaviour remain under development.

## Working scope

- Follow the current human assignment and read the relevant source brief before changing a component. Reading this file does not appoint an operating Chief of Staff or grant access to other workstreams.
- Distinguish proposed, implemented and verified behaviour. Do not describe a saved instruction as proof that a runtime loaded or followed it.
- Keep changes small and preserve successful behaviour. Record material uncertainty and the evidence needed to resolve it.

## Definition and data boundary

- Version reusable definitions, methods, configurable interfaces and synthetic examples. Keep credentials, personal/client records, private exports and runtime state outside tracked files.
- Inspect intended files before committing. Ignore rules prevent ordinary tracking of matching untracked files; they do not remove already committed content or enforce access control.
- Preserve third-party licence and attribution requirements. Public release and licence selection are separate human decisions.

## Available definitions

Read [README.md](README.md) for the purpose, operating model and current status. [SOUL.md](SOUL.md) holds shared identity and interaction guidance. [ROLES.md](ROLES.md) records agreed role types; individual contracts remain under development. [SKILLS.md](SKILLS.md) links the reusable methods prepared so far. Use the current human assignment for scope and authority. These files do not activate a role or deploy the harness.

## Communication

Use [Writing and Editing](skills/writing-and-editing/SKILL.md) and its [Writing and Editorial Standards](skills/writing-and-editing/references/EDITORIAL-STANDARDS.md) for authored or edited prose, reviews and advisory replies. Read the standard before the relevant work and reuse a current read during the task. Apply it alongside specialist workflows, preserving their scope and execution rules.

When delegating this work, include the current brief, relevant sources, accepted corrections and the shared skill and standard in the assignment. Do not assume a child agent inherits SOUL or the parent's loaded skills. Use the [role directory's handover rule](ROLES.md#coordination-and-shared-skills) before accepting or integrating its result.

## Emerging layout

README.md introduces the whole harness. Add files below when their content is ready and their separate use is clear:

- docs/ — reusable build method and shared operating contract. The detailed editorial standard lives inside the Writing and Editing skill package.
- examples/ — bounded assignments, synthetic cases and observable acceptance checks.
- modules/hidden-job-market/ — separable career workflow with explicit inputs and dependencies.

The Notion working design brief owns current design decisions until an explicit definition cutover. Domain services retain live records and checkpoints. Use authorised source references supplied with the task; report missing access rather than inventing their contents.