# Hermes Bots Group Settings Template

Copy this file for the role and link it from the sovereign sleeve under **Eval group**. Fill in the intended room and settings before giving the completed Markdown to Hermes. The role owner maintains it. Use the [Hermes setup guide](runtimes/hermes.md#set-up-an-eval-group) and the [evaluation guide](evaluating-role-groups.md) for the underlying method.

## Instructions for Hermes

Use this file as the entry point to install or refresh this role in Hermes.

1. Resolve the exact room, owning gateway and Master from **Room binding and orientation**. Use the [Hermes setup guide](runtimes/hermes.md#set-up-an-eval-group) if the room still needs to be commissioned.
2. Recover the selected shared role definition, private sleeve, relevant units of account, current brief and last checkpoint through the existing role binding. Follow [Bootstrap a role group](bootstrap-group.md) to connect and orient the Master and each participating room context. On a refresh, use the selected revisions in that binding. Adopt a new revision when the commission selects it.
3. Read the saved values and compare them with **Group chat settings**. For an install or refresh, apply any settings changes within the commission through supported owning-gateway controls and read them back. For a review, report the observed values and differences. Identify any field or source you could not verify or apply.
4. Return a short receipt with the role and room, selected source revisions, what loaded or was retrieved, the settings read back and any remaining gap. On first commissioning or when the dispatch route changes, verify a Master-to-room handoff and return. If no assignment is supplied, report readiness.

Give Hermes the completed file with this instruction:

> Install or refresh [role] in this Hermes group using [completed group Markdown]. Apply the selected role basis and declared room settings, recover the current checkpoint and report what you verified.

## Group chat settings

These headings match the Hermes settings dialog. The completed file supplies the exact text or selection for each field.

### Purpose

```text
[Role name]
```

### Shared notes

Replace the placeholders and adapt the role-specific wording before saving. Keep the saved notes within the dialog's 4,096-character limit.

```text
[Role]'s Master gives this group a specific question, the work to review and the evidence to use. For a relational eval, one peer takes [sovereign]'s position and the other takes the relevant counterpart's. Ask what each can see and decide, what they give and get, and what might change their next move. When first impressions matter, capture the counterpart's read before sharing our rationale.

[Harness reviewer] checks the role contract, latest steering, original evidence and relevant lived experience. Bring anything that could change the judgement into the discussion while the work can still change. Ask a pointed question or offer a supported correction. State what it changed or confirmed, and flag any unresolved disagreement. [Role]'s Master owns the recommendation to [sovereign].
```

### Who answers a message that names nobody

- **Reply routing** `lead`
- **Lead member** [Actual profile ID. For the Odin, Huginn and Muninn setup, select Odin. In Ben's Hermes connection, Odin's profile ID is `default`.]

The lead routes a new unaddressed message and can select one or more respondents. The lead can also answer. Explicit mentions address the named members directly. Confirm the saved routing and lead member through the owning gateway.

## Room binding and orientation

| Field | What to supply |
| --- | --- |
| Room and owning gateway | [Exact room ID, owning connection and private deployment record.] |
| Members and profiles | [Expected roster and actual profile IDs. Ben's standard roster is Odin (`default`), Huginn (`huginn`) and Muninn (`muninn`).] |
| Role and Master | [Sovereign sleeve and exact Master entry point. The role binding supplies the selected shared and private sources.] |
| Sources and experience | [Current brief, decision record, canonical resources and relevant lived experience through their maintained owners. Name the source access the group needs.] |

Verify which sources each actual room context loads at startup and which it retrieves for the work. Record any missing access needed for the case. Use the [package bootstrap](bootstrap.md) if the harness installation itself is missing or an update to it was commissioned.

## How the group works

- The Master commissions a bounded question with the artifact or decision, relevant evidence and the expected return. Use qualitative judgement and quantitative checks suited to the case.
- For a relational eval, the peers consider the sovereign and counterpart vantage points. If several counterparts matter, consider their decisions separately. When reciprocal paired work is commissioned, giver and active receiver describe how the peers contribute and take turns. Each retains a complete OODA loop.
- The harness reviewer checks that the group uses the selected contract, original evidence, steering and relevant lived experience. Surface missing context while it can still change the work. Return findings, evidence and unresolved differences to the Master. The Master owns the recommendation and records consequential decisions and reasons with the existing case or decision owner.

## Verify setup and handoff

Read back **Purpose**, **Shared notes**, reply routing, lead member and roster. When commissioning the group, use one unaddressed test post to verify who receives it. Verify required source access from each participating room context. Run one bounded Master-to-room handoff and return on real work. Record what was verified and any remaining gap with the deployment or case owner.
