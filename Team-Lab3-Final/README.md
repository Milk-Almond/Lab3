# Team Lab 3 — Emerging Technology Creation Agent

The confirmed team design is packaged with three saved model-authored analytical responses, source checks, a completed substantive Team Agent Record and comparison evidence. **Final post-test human team acceptance remains pending.** These are same-session Codex walkthroughs, not independent model API tests or evidence of production reliability.

## Review the submission materials

- [Team Agent Record](agents/creation_agent/records/team_agent_record.md)
- [Common-case comparison and retained limitation](agents/creation_agent/records/comparison_test_evidence.md)
- [Execution method and limits](agents/creation_agent/records/test_protocol.md)
- [Three saved responses](agents/creation_agent/responses/)
- [Original-source checks](agents/creation_agent/evidence/source_verification.md)
- [Confirmed contribution decisions](agents/creation_agent/records/decision_lineage.md)
- [Team Agent Inventory](TEAM_AGENT_INVENTORY.md) and [version record](VERSION_RECORD.md)
- [Validation log](agents/creation_agent/records/validation_results.txt)

## Reproduce structural checks

```bash
python tools/check_frozen_core.py
python agents/creation_agent/records/verify_package.py
```

These commands validate saved files; they do not call a model. To perform a fresh model run, use `tools/build_prompt.py` with an agent and case path, run the resulting prompt in your chosen model, and save its unedited response plus actual model/settings/date. The current prompts are retained under `agents/creation_agent/records/prompts/`.

Canonical editable agent files are under `agents/creation_agent/`. Root uploads and the original ZIP remain as provenance; the root source register and Team Agent Record mirror the current canonical records. Frozen Core is unchanged.

## Remaining human action

Review the linked outputs and limitations, confirm or correct final integration acceptance, and record any real dissent. Human source-review dates remain blank unless actually performed. Then submit the named GitHub commit, Team Agent Record and comparison/test evidence through the course submission page. No class attendance or 90%-in-class timing claim is made by this repository.
