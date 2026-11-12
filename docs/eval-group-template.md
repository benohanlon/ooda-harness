# Hermes Bots Group Settings Template

Copy this file for the role and link it from the sovereign sleeve under **Eval group**. Fill in the intended room and settings before giving the completed Markdown to Hermes. The role owner maintains it. Use the [Hermes setup guide](runtimes/hermes.md#set-up-an-eval-group) and the [evaluation guide](evaluating-role-groups.md) for the underlying method.

## Instructions for Hermes

Use this file as the entry point to install or refresh this role in Hermes.

1. Resolve the exact room, owning gateway and Master from **Room binding and orientation**. Use the [Hermes setup guide](runtimes/hermes.md#set-up-an-eval-group) if the room still needs to be commissioned.
2. Recover the selected shared role definition, private sleeve, relevant units of account, current brief and last checkpoint through the existing role binding. Follow [Bootstrap a role group](bootstrap-group.md) to connect and orient the Master and each participating room context. On a refresh, use the selected revisions in that binding. Adopt a new revision when the commission selects it.
3. Read the saved values from the owning gateway with `groups.state` and compare them with **Group chat settings**. For an install or refresh, apply changes within the commission through an authorised client that exposes `groups.context`. If the current bot context cannot save a field, give the operator the exact value to enter in Hermes **Room settings**, then read it back after the operator saves it. For a review, report the observed values and differences.
4. Return a short receipt with the role and room, the selected revisions, what each participant loaded at startup or retrieved for the work, the saved settings and any remaining gap. If no assignment is supplied, report setup status and carry any outstanding handoff or peer exchange into the first relevant eval.

Give Hermes the completed file with this instruction:

> Install or refresh [role] in this Hermes group using [completed group Markdown]. Apply the selected role basis and declared room settings, recover the current checkpoint and report what you verified.

## Group chat settings

These headings match the Hermes settings dialog. The completed file supplies the exact text or selection for each field.

### Purpose

Use up to 500 characters.

```text
[Role name]
```

### Shared notes

Replace the placeholders and adapt the role-specific wording before saving. Keep the saved notes within the dialog's 4,096 UTF-8 byte limit.

```text
[Role]'s Master gives this group a specific question, the work to review and the evidence to use. For a relational eval, one peer takes [sovereign]'s position and the other takes the relevant counterpart's. Ask what each can see and decide, what they give and get, and what might change their next move. When first impressions matter, capture the counterpart's read before sharing our rationale.

[Harness reviewer] checks the role contract, latest steering, original evidence and relevant lived experience. Bring anything that could change the judgement into the discussion while the work can still change. Ask a pointed question or offer a supported correction. State what it changed or confirmed, and flag any unresolved disagreement. [Role]'s Master owns the recommendation to [sovereign].
```

### Who answers a message that names nobody

- **Reply routing** `lead`
- **Lead member** [Resolve the intended lead's seated room member ID from the owning gateway. For the Odin, Huginn and Muninn setup, select Odin. Harry's room currently seats Odin as member `default`, mapped to profile `default`.]

The lead routes a new unaddressed human post and can select one or more respondents, including themselves. Direct mentions, room broadcasts and replies in an existing thread use their own routing. Confirm the saved routing and lead member through the owning gateway.

## Room binding and orientation

| Field | What to supply |
| --- | --- |
| Room and owning gateway | [Exact room ID, owning connection and private deployment record.] |
| Members and profiles | [Expected roster and observed member ID, profile ID and handle for each seat. Ben's standard roster is Odin, Huginn and Muninn.] |
| Role and Master | [Sovereign sleeve and exact Master entry point. The role binding supplies the selected shared and private sources.] |
| Sources and experience | [Current brief, decision record, canonical resources and relevant lived experience through their maintained owners. Name the source access the group needs.] |

Verify which sources each actual room context loads at startup and which it retrieves for the work. Record any missing access needed for the case. Use the [package bootstrap](bootstrap.md) if the harness installation itself is missing or an update to it was commissioned.

## How the group works

- The Master commissions a bounded question with the artifact or decision, relevant evidence and the expected return. Use qualitative judgement and quantitative checks suited to the case.
- For a relational eval, the peers consider the sovereign and counterpart vantage points. If several counterparts matter, consider their decisions separately. When reciprocal paired work is commissioned, giver and active receiver describe how the peers contribute and take turns. Each retains a complete OODA loop.
- The harness reviewer checks that the group uses the selected contract, original evidence, steering and relevant lived experience. Surface missing context while it can still change the work. Return findings, evidence and unresolved differences to the Master. The Master owns the recommendation and records consequential decisions and reasons with the existing case or decision owner.

## Verify setup and handoff

Read back **Purpose**, **Shared notes**, reply routing, lead member and roster. When lead routing is new, changed or unverified, check who receives a new unaddressed human post. Verify required source access from each participating room context. Run a bounded Master-to-room handoff and return on real work when the route is new, changed or still unverified. When reciprocal peer work is commissioned, record one substantive peer exchange and what it changed or confirmed. Keep pending checks with the deployment or case owner until observed.
