# Gauntlet Loop

Matt Shumer’s Gauntlet Loop combines a [gauntlet](gauntlets.md) with repeated revision. The builder makes a version. A critic examines that version against a concrete reference. The critic’s finding determines what the builder changes next. Use it when the comparison can reveal a material defect and another pass is worth the effort. [Original method](https://somethingbig.ai/gauntlet-loop)

## Design the comparison

Choose a reference the critic can actually inspect and state which quality matters. For a setup guide, for example, the bar might be whether a first-time user can reach a working installation from a clean environment. A competing guide’s length or visual polish tells us little about that outcome.

Give the lead the goal, reference and constraints. Let it identify parts that can be judged independently. Give each critic the brief, reference and actual output in fresh context. Withhold the builder’s rationale and hide which version is which when a blind comparison makes sense.

## Run and judge

The critic returns a verdict, the most consequential gap and the evidence that exposed it. The builder revises the work. The next critic inspects the revision under the same conditions. In the setup-guide example, return the first instruction where a new user gets stuck, then repeat the setup from that point of failure in a clean environment.

Keep the artifact and comparison results together so the owner can inspect progress. Stop when the work meets the agreed bar, further gains cease to matter, the owner intervenes or the available budget is spent. If separate parts pass, check that the assembled result still works for its intended user.

## Reusable brief

> Produce **[artifact]** for **[user and outcome]**. Compare it with **[reference or test]** on **[quality that matters]**. Work within **[authority and budget]**. Have an independent critic inspect the result and return the largest evidenced gap to the builder. Recheck each revision. Return the integrated result, comparison evidence and remaining limits to **[owner]**.

[General loop design](loops.md) · [Engineering references](../lists/harness-engineering-resources.md#loop-design)
