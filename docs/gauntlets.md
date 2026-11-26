# Gauntlets

In OODA, a gauntlet is a set of challenges used to judge a piece of work or a system against a stated standard. One pass produces evidence and a verdict. The owner can accept the result, decline it or commission a revision. A [loop](loops.md) forms when the verdict guides another attempt and the revised work comes back for assessment.

## Design a gauntlet

| Question | What to specify |
| --- | --- |
| What decision will this support? | Name the candidate version, intended use and decision owner. |
| What must it withstand? | Choose representative cases, including a difficult case or known failure. State the expected behaviour and which failures would change the decision. |
| How will each challenge be judged? | Identify the evidence, criterion and judge. Use direct checks where possible and an independent reviewer where judgement matters. |
| What comes back? | Record the observed result for each challenge, any missing evidence and the overall verdict. Give the owner enough detail to act on a failure. |

For example, test a new handover by asking a fresh worker to recover an existing case, identify who owns the next action and recognise a deliberate wait. Supply the normal starting context and withhold the answers. Compare its return with the case record. That completes one gauntlet. If the owner revises the handover, repeat comparable cases and check that earlier successes still hold.

## When revision is part of the commission

[Matt Shumer’s Gauntlet Loop](gauntlet-loop.md) couples independent comparison to revision. Use that pattern when a builder can act on the critic’s findings and another pass is worth the effort. [Original method](https://somethingbig.ai/gauntlet-loop)

## Materials for designers

| Source | What to borrow |
| --- | --- |
| [Hugging Face EvaluationSuite](https://huggingface.co/docs/evaluate/evaluation_suite) | Run several tasks on one candidate and retain each score. One run establishes a baseline. |
| [OpenAI evaluation practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Choose representative cases and calibrate automated grading against human judgement. Use the [optimisation guide](https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy) when changing the candidate between runs. |
| [Anthropic’s outcome-grader walkthrough](https://platform.claude.com/cookbook/managed-agents-cma-verify-with-outcome-grader) | Specify the evidence the grader must inspect. In the worked case, opening the cited filing exposed the wrong kind of document. |
| [Hermes two-stage review](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/software-development/software-development-subagent-driven-development) | Check conformance to the brief and quality separately. Returning a failed stage to the implementer adds a revision loop. |
| [Nous Research AutoReason](https://github.com/NousResearch/autoreason#method) | When comparing revisions, include the original among the blind-ranked candidates. This allows a sound original to survive an unhelpful edit. |

These sources describe evaluation and refinement practices under their own names. The OODA definition above supplies the shared vocabulary.
