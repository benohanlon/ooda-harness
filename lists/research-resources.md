# Research Resources

Places to find research and selected sources used in the harness. Browse the links first, then use the source notes for reading guidance, evidence and limitations.

## Contents

- [Libraries, repositories and search](#libraries-repositories-and-search)
- [Selected sources](#selected-sources)
- [Source notes](#source-notes)

## Libraries, repositories and search

### Academic research

- [Google Scholar](https://scholar.google.com/) - Search scholarly literature and follow citations or available full-text copies.
- [arXiv](https://arxiv.org/) - Research preprints, including AI and computer science. Reading does not require an account.
- [Zenodo](https://zenodo.org/) - Research publications, datasets, software and other deposited outputs.
- [ResearchGate](https://www.researchgate.net/) - Researchers' publications and available full texts. Access varies by item.
- [Academia.edu](https://www.academia.edu/) - Papers, chapters and other shared scholarly documents. Some access requires an account.

### Books and documents

- [Internet Archive](https://archive.org/) - Digitised books, documents and archival collections.
- [Open Library](https://openlibrary.org/) - Book catalogue with edition details and reading or borrowing routes.
- [Scribd](https://www.scribd.com/) - Community-uploaded documents, including papers and manuals. Download access can require a subscription.

### Curated directories

- [Awesome](https://github.com/sindresorhus/awesome) - Topic directories for finding specialised collections of tools and resources.

For AI papers, models, datasets and practitioner discussion, use the Hugging Face and Nous/Hermes links in [Community Hubs](../skills/community-research/references/communities.md#browse-hubs).

Directory entries were checked on 23 October 2026. They are discovery routes, not claims that their contents have been read or adopted. Follow a useful result to its original author, version and relevant text.

## Selected sources

### Orientation

- [The Essence of Winning and Losing](https://slightlyeastofnew.com/wp-content/uploads/2010/03/essence_of_winning_losing.pdf) - Boyd's short presentation and complete OODA sketch. ([notes](#john-boyd-the-essence-of-winning-and-losing))
- [Boyd's Real OODA Loop](https://slightlyeastofnew.com/wp-content/uploads/2018/05/boyds-real-ooda-loopx.pdf) - Richards on orientation, coordination and business application. ([notes](#chet-richards-boyds-real-ooda-loop))

### Learning and feedback

- [Reflexion](https://arxiv.org/html/2303.11366v4) - Feedback and retained reflections across later attempts. ([notes](#shinn-and-colleagues-reflexion))
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/pdf/2310.01798) - Limits of critique and retry without useful external feedback. ([notes](#huang-and-colleagues-large-language-models-cannot-self-correct-reasoning-yet))
- [ReHarness](https://arxiv.org/html/2610.12668v1) - Revising retained lessons when later evidence arrives. ([notes](#xiao-and-colleagues-reharness))
- [Exploration and Exploitation in Organizational Learning](https://hiveresearchlab.org/wp-content/uploads/2013/12/march_1991_exploration_and_exploitation_in_organizational_learning.pdf) - How convergence can crowd out useful exploration. ([notes](#james-march-exploration-and-exploitation-in-organizational-learning))

### Evaluation and coordination

- [AI Agents That Matter](https://arxiv.org/pdf/2407.01502) - Cost-controlled comparisons and strong baselines. ([notes](#kapoor-and-colleagues-ai-agents-that-matter))
- [Ironies of Automation](https://tc.ifac-control.org/4/1/newsletter/ironies-of-automation/@@download/file/Bainbridge1983_Automatica_Ironies%20of%20automation.pdf) - Human monitoring, skill and recovery burdens. ([notes](#lisanne-bainbridge-ironies-of-automation))
- [Agent-system scaling study](https://arxiv.org/html/2512.08296v3) - Coordination architectures, task differences and budget controls. ([notes](#google-research-agent-system-scaling-study))
- [Harness design for long-running apps](https://www.anthropic.com/research/harness-design-long-running-apps) - Maker/evaluator collaboration and shared criteria. ([notes](#anthropic-harness-design-for-long-running-apps))

### Hermes runtime

- [Hermes delegation](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation) - Context loading, steering, completion and recovery. ([notes](#hermes-delegation-documentation))

## Source notes

**Maintained owner:** Research Lead. This shelf carries selected reusable sources already used in harness research. It complements [Community Hubs](../skills/community-research/references/communities.md), which locates ongoing practitioner evidence.

**Coverage basis:** the 22 October 2026 engineering review and its retained source coverage. Entries below report that recorded reading, not a new full read by every consumer. Reading is separate from adoption or a reproduced result. Retrieve the specified original passages when the current task depends on them. Follow the [Community Research method](../skills/community-research/SKILL.md) for new practitioner inquiry.

The links lead to public original or full-text routes inspected during that research. Live availability can change. Report missing access rather than substituting an unseen source. No PDFs or licensed archives are bundled here.

### OODA and orientation

#### John Boyd: The Essence of Winning and Losing

- **Original:** [six-page presentation, 1996 / edited 2012](https://slightlyeastofnew.com/wp-content/uploads/2010/03/essence_of_winning_losing.pdf).
- **Retrieve when:** an operating method treats OODA as a fixed sequence, or needs to explain orientation, feedback and interaction with an unfolding situation.
- **Read:** the whole short presentation and its complete OODA sketch on PDF page 4, including feedback and implicit guidance.
- **Recorded coverage:** all six pages' text and the full sketch were inspected. This is a strategic formulation, not empirical evidence that a particular AI architecture works.

#### Chet Richards: Boyd's Real OODA Loop

- **Original:** [2018 paper](https://slightlyeastofnew.com/wp-content/uploads/2018/05/boyds-real-ooda-loopx.pdf).
- **Retrieve when:** applying Boyd's account to coordination and business work, or clarifying the role of orientation.
- **Read:** relevant discussion and diagrams, particularly PDF pages 11–12 and 17–28.
- **Recorded coverage:** those sections were read completely and the page index was screened. The full 44 pages were not reread in that review. This is interpretation and application of Boyd, not an AI runtime test.

### Feedback, learning and useful judgement

#### Shinn and colleagues: Reflexion

- **Original:** [version 4 full text](https://arxiv.org/html/2303.11366v4).
- **Retrieve when:** designing how explicit feedback and retained reflections may change later attempts.
- **Read:** method, task setups, results, ablations and limitations, especially the feedback source and memory use.
- **Recorded coverage:** main methods and results corresponding to PDF pages 2–9 were reviewed. Code and appendices were not reproduced. The selected tasks and feedback conditions limit transfer to this harness.

#### Huang and colleagues: Large Language Models Cannot Self-Correct Reasoning Yet

- **Original:** [paper](https://arxiv.org/pdf/2310.01798).
- **Retrieve when:** assessing claims that another critique or retry necessarily improves correctness.
- **Read:** problem setup, result tables, matched debate/prompt comparison and limitations.
- **Recorded coverage:** PDF pages 1–5 and 7–9 were reviewed. No tests were reproduced. Historical reasoning-model results do not settle current models, preference tasks or this proposed reciprocal pair.

#### Xiao and colleagues: ReHarness

- **Original:** [version 1 full text](https://arxiv.org/html/2610.12668v1).
- **Retrieve when:** deciding how later evidence should revise a retained lesson without erasing the original event.
- **Read:** framework and Figure 1, results, ablations and discussion, especially feedback quality, grounding and cost.
- **Recorded coverage:** framework and main findings corresponding to PDF pages 3–10 and Figure 1 were inspected. Appendices were not newly reread. Benchmark results and model-judged grounding do not validate automatic conclusions from unanswered real-world messages.

#### James March: Exploration and Exploitation in Organizational Learning

- **Full text:** [1991 paper](https://hiveresearchlab.org/wp-content/uploads/2013/12/march_1991_exploration_and_exploitation_in_organizational_learning.pdf).
- **Retrieve when:** rapid convergence or easily measured feedback could crowd out exploration and useful alternatives.
- **Read:** model assumptions and interpretation, including PDF pages 2–5 and 16–17.
- **Recorded coverage:** those passages were reviewed. This is a simplified organisational model. Its application to agent research is an interpretation to test, not a prescribed allocation policy.

### Evaluation, coordination and human effort

#### Kapoor and colleagues: AI Agents That Matter

- **Original:** [paper](https://arxiv.org/pdf/2407.01502).
- **Retrieve when:** planning a comparison between a paired role and a strong single-agent baseline.
- **Read:** cost-controlled comparisons, baseline method, human involvement and evaluation limitations.
- **Recorded coverage:** PDF pages 2–4 and 9–11 were reviewed. Appendices were indexed rather than reaudited. Use it to frame an evaluation; no local performance result follows from reading it.

#### Lisanne Bainbridge: Ironies of Automation

- **Full text:** [1983 paper, IFAC-hosted copy](https://tc.ifac-control.org/4/1/newsletter/ironies-of-automation/@@download/file/Bainbridge1983_Automatica_Ironies%20of%20automation.pdf).
- **Retrieve when:** automation reduces routine involvement but may leave the human with harder monitoring, interpretation or recovery work.
- **Read:** the complete short paper, including skill, monitoring and collaboration discussion.
- **Recorded coverage:** the complete retained five-page text was reread. Its evidence concerns process control. Implications for modern AI need to be examined in actual human work.

#### Google Research: agent-system scaling study

- **Original:** [arXiv:2512.08296, version 3](https://arxiv.org/html/2512.08296v3).
- **Retrieve when:** choosing coordination architecture or evaluating whether added agents justify their effort.
- **Read:** system definitions, task and architecture comparisons, budget controls, limitations and Appendix E implementation controls.
- **Recorded coverage:** those sections were reviewed without code execution. The study does not directly test this harness's two reciprocal qualitative participants. Use the pinned paper version rather than mixing figures from earlier summaries.

#### Anthropic: Harness design for long-running apps

- **Original:** [research report](https://www.anthropic.com/research/harness-design-long-running-apps).
- **Retrieve when:** designing maker/evaluator collaboration, shared criteria or review of subjective outputs.
- **Read:** subjective frontend examples, full-stack contracts, simplification and dependence on task/model capability.
- **Recorded coverage:** these methods and examples were inspected. Practitioner cases offer design evidence, with limited causal isolation. They do not establish a universal generator/evaluator architecture.

### Runtime behaviour

#### Hermes: delegation documentation

- **Official source:** [delegation](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation).
- **Retrieve when:** establishing peer contexts, instruction inheritance, steering, completion or recovery in Hermes.
- **Read:** current context-loading, capability inheritance, steering, completion and lifetime sections. Compare with the installed version and observed behaviour.
- **Recorded coverage:** those sections were inspected in the engineering review. Documentation was not a test of this installation. A defined pair still requires verified loading, received and applied contributions, action ownership and restoration.

### Retaining and applying a source

Keep the author's claim, relevant original passage and our interpretation distinguishable. Record conflicting evidence and material limits. When a finding changes work, link its decision, method and later result in the existing work record. A source can remain useful background without becoming an operating instruction.

Update the relevant entry when coverage changes or a route is superseded. Private reference shelves, books-to-read, ideas and hypotheses retain their own owners. This selected shelf does not replace them or imply that every linked source has been read in full.
