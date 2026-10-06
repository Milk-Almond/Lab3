# Test protocol and execution provenance

Date: 2026-10-06 (America/New_York). Agent: team-1.0.0. Instruction/case baseline: d4ddb139789c6fef8f9e8b4334f73a759b0df312.

## Method actually used

The current Codex assistant read the common instructions, specialist instructions, metadata, schema and all three case inputs, consulted the six original-source abstract pages, then generated the three saved JSON responses while applying those instructions. This is an actual model-authored, same-session analytical walkthrough, not a separate model API execution or an isolated test session. The source evidence list was reused across responses because the source packet is identical; analytical fields were written separately. Python serialized the assistant-authored content; it did not run an LLM.

The complete prompt packets constructed by the unmodified course builder are preserved under `prompts/`. All their constituent contents were available to the assistant; they were not sent through a separate API. Outputs are under `../responses/`. The first saved outputs are retained without subsequent content repairs. No model snapshot identifier, temperature, random seed or token limit is exposed for this session, so these are recorded as unavailable rather than invented. There was one saved response per case, with no repeated trials.

The same assistant generated and reviewed the responses. It knew the test purposes, other cases and intended boundaries. Thus this is not independent, blinded, held-out or statistically reproducible performance evidence. It tests analytical form and qualitative application of the instructions, not executable procurement/marketing tools or operational permission enforcement.

## Review criteria derived from existing specialist instructions

1. Separate historical need, predecessors and enablers from the present business need.
2. Preserve source-supported history across contexts; distinguish evidence, inference and assumptions.
3. Map inherited capabilities to tasks and limitations, and compare simpler alternatives.
4. Tie contextual differences to supplied constraints and consequence levels.
5. Retain boundaries, differentiated confidence, value conditions and observable triggers.
6. Preserve general history but abstain from unsupported autonomous approval when context is missing.

Structural validation is separate from these qualitative judgments. `verify_package.py` checks the schema constructs actually used by the frozen schemas, prompt regeneration, input/output metadata, source IDs and evidence completeness. `validation_results.txt` preserves command output. It does not prove substantive correctness.
