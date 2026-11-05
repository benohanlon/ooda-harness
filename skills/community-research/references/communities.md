# Community Hubs

Places to find AI and harness-engineering practitioners, implementations and discussion. Browse the links, then consult the hub notes for the relevant question and recorded coverage.

Bundled copy of [the canonical Community Hubs](../../../lists/community-hubs.md), retained for standalone Community Research use. The harness's [Lists](../../../LISTS.md) is the complete shared catalogue. Research Lead maintains this collection. Harness Engineering checks technical routes and compatibility when using or changing them.

## Contents

- [Browse hubs](#browse-hubs)
- [Hub notes](#hub-notes)

## Browse hubs

### Nous Research and Hermes

- [Nous Research](https://nousresearch.com/) - Research and the wider Nous ecosystem.
- [Hermes documentation](https://hermes-agent.nousresearch.com/docs) - Official setup, features and developer guidance.
- [Hermes on GitHub](https://github.com/NousResearch/hermes-agent) - Source code, issues and implementation discussion.
- [Nous Discord](https://discord.com/invite/nousresearch) - Practitioner discussion, including plugins, skills and skins. Access requires joining the server.
- [Skills Hub](https://hermes-agent.nousresearch.com/marketplace?kind=skills) - Discover reusable Hermes skills.
- [Plugin Catalog](https://hermes-agent.nousresearch.com/marketplace?kind=plugins) - Discover Hermes plugins.

### Codex, Claude and cross-runtime engineering

- [Harness Engineering Resources](../../../lists/harness-engineering-resources.md) - Official documentation, source and extension routes for Hermes, Codex and Claude, plus reviewed implementations and professional waypoints.
- [OpenAI plugin directory](https://developers.openai.com/plugins) - Discover published plugins and check supported products and surfaces.
- [Claude Code documentation index](https://code.claude.com/docs/llms.txt) - Find current official references before making capability claims.

### Hugging Face

- [Hugging Face](https://huggingface.co/) - Models, datasets, Spaces and community contributions.
- [Daily Papers](https://huggingface.co/papers) - Discover AI papers and follow their original sources.
- [Community forum](https://discuss.huggingface.co/) - Practitioner questions and technical discussion.
- [OpenEvals](https://huggingface.co/OpenEvals) - Evaluation resources and community benchmark work.
- [Community Evals / EvalEval Coalition](https://huggingface.co/blog/eee-community-evals) - Evaluation provenance and community contributions.

### Evaluation, harness engineering and memory

- [Parlance Labs](https://parlance-labs.com/blog/posts/auto-evals/) - Evaluation methods and practitioner examples.
- [Learn Harness Engineering](https://walkinglabs.github.io/learn-harness-engineering/en/) - Practical exercises and source trails.
- [Awesome Harness Engineering](https://github.com/walkinglabs/awesome-harness-engineering) - Curated routes to harness-engineering resources.
- [Agent Memory Repo](https://github.com/AgentMemoryRepo/agentmemoryrepo) - Implementation and contributor discussion around agent memory.
- [Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) - Knowledge representation and provenance specification.

General Hugging Face and Nous/Hermes entry points were checked on 23 October 2026. The recorded coverage below applies to the named sources and discussions, not every linked hub or private channel. For books, papers and document repositories, use [Research Resources](../../../lists/research-resources.md).

## Hub notes

**Maintained owner:** Research Lead. **Coverage basis:** source and discussion reviews recorded on 22 October 2026. These are selected routes, not an exhaustive directory or live coverage claim. Refresh the relevant route when using it for a current decision. Private channels require supplied access and remain outside the public record.

Use the [Community Research method](../SKILL.md) to follow the routes. The entry describes where to look; it does not endorse the claims found there.

### Nous Research and Hermes practitioners

**Use when:** deciding whether Hermes already supports a proposed method, investigating recurring runtime failures, or finding maintained skills and plugins.

Start with the [official contribution guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing), [Skills Hub](https://hermes-agent.nousresearch.com/marketplace?kind=skills) and [Plugin Catalog](https://hermes-agent.nousresearch.com/marketplace?kind=plugins). Follow the relevant implementation and its version. The contribution guide points to [Nous Discord](https://discord.com/invite/nousresearch), including practitioner discussion of plugins, skills and skins. Retrieve relevant discussion only if access is available.

The [Hermes configuration discussion](https://www.reddit.com/r/hermesagent/comments/1x24qfp/my_hermes_configuration_that_works_for_me/) is a retained practitioner trail. Read the proposed configuration and substantive replies about maintenance, regressions and built-in alternatives. Check current [Curator documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/curator) before proposing another maintenance mechanism.

**Recorded coverage and limits:** official routes and the Reddit original with visible replies were inspected in the source review. Discord conversations were not inspected. Practitioner reliability claims were not reproduced. Public documentation or a catalogue entry does not prove installation or behaviour in this harness.

### Hugging Face OpenEvals

**Use when:** investigating evaluation provenance, task-specific benchmarks, retained traces or executable checks.

Follow [OpenEvals](https://huggingface.co/OpenEvals) and [Community Evals / EvalEval Coalition](https://huggingface.co/blog/eee-community-evals) to the relevant paper, dataset, model card, code and discussion. One retained implementation trail is [Thinkingbox's paper page](https://huggingface.co/papers/2608.19741) to [Microsoft Thinkingbox](https://github.com/microsoft/thinkingbox).

**Recorded coverage and limits:** public primary-resource follow-up inspected these routes. Thinkingbox projects were not executed; framework availability and full scenario-data availability are separate. A paper listing or score does not establish transfer to our role assignments. Some resources or discussions may require an account or additional access.

### Evaluation practitioners

**Use when:** deciding what counts as a useful failure, calibrating semantic judgement against human examples, or checking whether a reviewer damages good work.

Use Antaripa Saha and Hamel Husain's [Parlance Labs article on automatic evaluations](https://parlance-labs.com/blog/posts/auto-evals/) as a primary starting route. Read the treatment of human annotation, evolving criteria, missed failures, false criticisms and new discoveries. Follow the authors' cited experiments and implementations where they bear on the assignment.

**Recorded coverage and limits:** the primary article and selected practitioner discussion were reviewed. This is methodological guidance, not a deployed evaluator or proof that one scoring scheme fits every task. Public article access does not imply access to paid teaching or private communities.

### Walking Labs

**Use when:** finding practical harness-engineering exercises or source trails for continuity, verification and maker/checker patterns.

Use [Learn Harness Engineering](https://walkinglabs.github.io/learn-harness-engineering/en/) and its [repository](https://github.com/walkinglabs/learn-harness-engineering). Select the lecture or project that addresses the question. The [curated source list](https://github.com/walkinglabs/awesome-harness-engineering) and [contribution rules](https://github.com/walkinglabs/awesome-harness-engineering/blob/main/CONTRIBUTING.md) provide routes to originals and an example of source selection.

**Recorded coverage and limits:** overview, relevant methods and source-selection routes were inspected. Projects were not executed. This material synthesises other authors and is not independent replication. No Discord invitation was verified.

### Agent Memory Repo and Open Knowledge Format contributors

**Use when:** investigating source attribution, freshness, generated versus verified knowledge, or correction and lifecycle design.

Follow the [Agent Memory Repo introduction](https://cognition.com/agent-memory-repo) and [repository](https://github.com/AgentMemoryRepo/agentmemoryrepo). A retained contributor trail runs through [RFC #9](https://github.com/AgentMemoryRepo/agentmemoryrepo/issues/9) to [Open Knowledge Format's specification](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) and the [OKF-Runtime skill](https://github.com/spomytkin/OKF-Runtime/blob/main/SKILL.md). Read the exact proposal, implementation status and relevant provenance fields.

**Recorded coverage and limits:** release material, the issue and downstream specifications were inspected in the source review. The interoperability proposal was not established as an accepted integration. Hermes compatibility and runtime quality were not tested. A useful provenance idea does not require adopting another authoritative memory store.

### Maintaining this directory

Retain a route when it answers a recurring question or opens a useful line of inquiry. Record changed locations, unavailable access or superseded methods with the relevant evidence. Keep source reading separate from adopted operating policy. Broader GTM, career and open-research trails remain with the assigned domain's source owner until a reusable route is deliberately selected for this package.
