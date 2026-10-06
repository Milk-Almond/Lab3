# Team Emerging Technology Creation Agent

Drop this `agents/creation_agent/` folder into the course scaffold.

## Important

Do **not** overwrite or modify `core/input_schema.json`, `core/output_schema.json`, or any other Frozen Core file.

## Core behavior

The agent separates:
1. ET generally;
2. ET for the application; and
3. ET for the application in the organization.

The general creation history should remain materially stable when technology and evidence are unchanged. Context changes the relevance, consequence and acceptable authority of inherited capabilities—not the historical record.

## Test files

- `cases/primary.json` — industrial procurement exception support.
- `cases/contrast_1.json` — same technology in lower-consequence marketing work.
- `cases/boundary_missing_context.json` — autonomous approval request with consequential context intentionally missing.

## Typical scaffold workflow

From the scaffold root, use the course-provided tools, for example:

```bash
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/creation_agent --case agents/creation_agent/cases/primary.json
# Run the generated prompt through the model and save the JSON response.
python tools/validate_response.py agents/creation_agent/responses/primary_response.json
```

Repeat for the contrast and boundary cases.

## Evidence

`evidence/source_register.json` is a starting register. Before submission, the team should open the original/authoritative sources and record its own access/check dates. Do not claim verification solely because another candidate checked a source.

## Team provenance

See `records/decision_lineage.md`. The synthesis adopts:
- mp7240-sudo: analytical backbone and evidence/applicability discipline;
- yanisimova: historical/context boundary and epistemic safeguards;
- Harry-max264: capability-task-limitation and simpler-alternative tests;
- sawulya: explicit value condition;
- yicrry777: common scaffold compatibility only from the reviewed state.
