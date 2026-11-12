# Hermes Bots Group Settings Template

Copy this file for a selected role and link it from the sovereign sleeve under **Eval group**. The role owner maintains the completed copy.

## Apply this template to a role

1. Link the selected shared role definition, private sleeve and Master. In the private copy, link to the setup, bootstrap and eval guides at the selected shared revision or to an accessible snapshot. The source links in this template are relative to the shared repository.
2. For a new group, choose the Hermes connection and bot profiles, then create the room and record its ID using the [Hermes setup guide](runtimes/hermes.md#set-up-an-eval-group). For an existing group, verify its room ID, owning gateway and roster.
3. Fill in the room settings, name the member who represents the harness, and record how the Master sends work and receives findings. Give the completed file to Hermes using the instruction below. If the handoff is still pending, carry it into the first real eval. Use the [evaluation guide](evaluating-role-groups.md) for the review method.

## Instructions for Hermes

Use this file as the entry point to install or refresh this role in Hermes.

1. Resolve the exact room, owning gateway and Master from **Room binding and orientation**. Use the [Hermes setup guide](runtimes/hermes.md#set-up-an-eval-group) if the room still needs to be commissioned.
2. Use the role's selected shared definition, private sleeve, relevant units of account and current brief. Recover the last checkpoint if one exists. Follow [Bootstrap a role group](bootstrap-group.md) to orient each participating room context and connect it to the Master. On a refresh, use the revisions selected in the binding or explicitly selected for this commission.
3. Read the saved values from the owning gateway with `groups.state` and compare them with **Group chat settings**. For an install or refresh, apply changes within the commission through an authorised client that exposes `groups.context`. If the current bot context cannot save a field, give the operator the exact value to enter in Hermes **Room settings**, then read it back after the operator saves it. If the current context cannot read the saved settings either, ask the operator for the saved values from the settings view and record the source of the readback. For a review, report the observed values and differences.
4. Return a short receipt with the role and room, the selected revisions, what each participant loaded at startup or retrieved for the work, the saved settings and any remaining gap. If no assignment is supplied, report setup status and carry any outstanding handoff or peer exchange into the first relevant eval.

Give Hermes the completed file with this instruction:

> Install or refresh [role] in this Hermes group using [completed group Markdown]. Apply the selected role basis and declared room settings, resume from the current checkpoint if there is one, and report what you verified.

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
[Role]'s Master gives the group a specific question, the work to review and the evidence to use. For a relational eval, use the role contract to identify the actors and the decision in play. One peer takes [sovereign]'s vantage point and the other takes the relevant counterpart's. Ask how each sees the situation and the other party, what each can decide, what they give, get or risk, and which incentives, trade-offs or constraints might change their next move. When first impressions matter, capture the counterpart's read before sharing our rationale. Treat these readings as hypotheses to test against evidence and actual responses.

[Harness reviewer] represents the harness in every eval. Check that the group is applying the selected role contract, latest steering and relevant standards. Recover decision-changing context from original evidence, prior decisions, accepted corrections and lived experience, especially after a diversion, handoff or compaction. Check how that context is being used. While the work can still change, ask a pointed question or make a supported correction. Say what it changed or confirmed and flag unresolved disagreement. [Role]'s Master owns the recommendation to [sovereign].
```

### Who answers a message that names nobody

- **Reply routing** [Select the room's routing mode. Use `lead` when a designated member should route new unaddressed human posts.]
- **Lead member** [For `lead` routing, resolve the designated lead's seated room member ID from the owning gateway.]

The lead routes a new unaddressed human post and can select one or more respondents, including themselves. Direct mentions, room broadcasts and replies in an existing thread use their own routing. Confirm the saved routing and lead member through the owning gateway.

## Room binding and orientation

| Field | What to supply |
| --- | --- |
| Room and owning gateway | [Exact room ID, owning connection and private deployment record.] |
| Members and profiles | [Expected roster and observed member ID, profile ID and handle for each seat. Name the peers and the harness reviewer. The reviewer can also be the routing lead.] |
| Role and Master | [Selected shared definition, sovereign sleeve and exact Master entry point.] |
| Dispatch and return | [How the Master sends work to this room and receives findings. Link to the mechanism and its verification, or mark it pending.] |
| Sources and experience | [Current brief, decision record, canonical resources and relevant lived experience through their maintained owners. Name the source access the group needs.] |

Verify which sources each actual room context loads at startup and which it retrieves for the work. Record any missing access needed for the case. Use the [package bootstrap](bootstrap.md) if the harness installation itself is missing or an update to it was commissioned.

## How the group works

- The Master commissions a bounded question with the artifact or decision, relevant evidence and the expected return. Use qualitative judgement and quantitative checks suited to the case.
- For a relational eval, the peers consider the sovereign and counterpart vantage points. If several counterparts matter, consider their decisions separately. When reciprocal paired work is commissioned, giver and active receiver describe how the peers contribute and take turns. Each retains a complete OODA loop.
- The harness reviewer checks how the group reached its judgement and whether it applied the relevant role guidance and memory. Bring forward the context that could change the work and show what it changed or confirmed. The Master receives the findings and unresolved differences, owns the recommendation and records consequential decisions and reasons with the existing case or decision owner.

## Verify setup and handoff

Read back **Purpose**, **Shared notes**, reply routing, lead member and roster. When lead routing is new, changed or unverified, check who receives a new unaddressed human post. Verify required source access from each participating room context. Run a bounded Master-to-room handoff and return on real work when the route is new, changed or still unverified. When reciprocal peer work is commissioned, record one substantive peer exchange and what it changed or confirmed. Keep pending checks with the deployment or case owner until observed.
