# Repository contribution guidance

This repository is the private development home for OODA Harness. Its initial README is a placeholder; reusable operating rules and runtime behaviour are still being designed.

## Working scope

- Follow the current human assignment and read the relevant source brief before changing a component. Reading this file does not appoint an operating Chief of Staff or grant access to other workstreams.
- Distinguish proposed, implemented and verified behaviour. Do not describe a saved instruction as proof that a runtime loaded or followed it.
- Keep changes small and preserve successful behaviour. Record material uncertainty and the evidence needed to resolve it.

## Definition and data boundary

- Version reusable definitions, methods, configurable interfaces and synthetic examples. Keep credentials, personal/client records, private exports and runtime state outside tracked files.
- Inspect intended files before committing. Ignore rules prevent ordinary tracking of matching untracked files; they do not remove already committed content or enforce access control.
- Preserve third-party licence and attribution requirements. Public release and licence selection are separate human decisions.

## Emerging layout

README.md introduces the whole harness. Add files below when their content is ready and their separate use is clear:

- docs/ — reusable build method and shared operating contract, including the detailed voice core.
- examples/ — bounded assignments, synthetic cases and observable acceptance checks.
- modules/hidden-job-market/ — separable career workflow with explicit inputs and dependencies.

The Notion working design brief owns current design decisions until an explicit definition cutover. Domain services retain live records and checkpoints. Use authorised source references supplied with the task; report missing access rather than inventing their contents.
