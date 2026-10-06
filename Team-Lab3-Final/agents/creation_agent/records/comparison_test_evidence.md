# Common-case comparison and retained limitation

Reviewer: same Codex assistant that generated the outputs. Qualitative review, not independent assessment. See `test_protocol.md` for execution limits.

| Criterion | Primary procurement response | Marketing contrast response | Review |
|---|---|---|---|
| General history | Transformer, retrieval, few-shot adaptation, instruction following, reasoning/action and API use; dated sources S1–S6 | Same milestones and technical lineage, different wording | Materially stable; no organization-specific origin story |
| Historical need vs current need | Research problems distinguished from procurement exceptions | Research problems distinguished from incomplete briefs | Present business problems are not claimed as historical causes |
| Application mapping | Policies, permitted records, missing information and buyer summaries | Brand guidance, incomplete briefs and editor drafts | Same capabilities map to different tasks and failure modes |
| Context facts | Versioned policies, sensitive supplier data, limited integration, buyer authority | Reversible drafts, editor review, light integration, internal material | More than two supplied constraints used in each case |
| Management implication | Read-only exception-support comparison; preserve deterministic routines | Bounded internal drafting comparison; no publishing authority | Change justified by consequences and workflow, not changed history |
| Simpler alternatives | Checklist/search and retrieval plus non-agentic LLM | Brief checklist/search and retrieval plus conventional LLM | Iteration must demonstrate incremental benefit |
| Evidence status | Historical sources; application inferences; hypothetical organization | Same distinctions | No company baseline or ROI invented |
| Scope | No purchasing authority/readiness/ROI conclusion | No publication authority/readiness/ROI conclusion | Handoffs remain explicit |

## Traceable output examples

- Primary `organization_specific_finding`: “read-only does not mean harmless.” The reason is consequential purchases and sensitive information, even when the model cannot transact.
- Contrast `organization_specific_finding`: “Internal brand material is not public data”. Lower draft consequences do not eliminate confidentiality requirements.
- Both `value_opportunity_implication` fields require measured advantage over simpler workflows; neither reports a measured gain.
- Boundary `abstention_or_more_information_needed`: “Abstain from deciding whether this organization should allow autonomous exception approval.” The general historical finding is retained, while policy ownership, permissions and consequences are requested.

## Remaining limitation preserved: cue dependence and weak generalization evidence

Observed in the actual inputs and outputs: `boundary_missing_context.json` explicitly instructs the model to preserve history and abstain, and all cases embed source summaries with warnings against overclaiming. The saved boundary response complies, but that result does not establish spontaneous boundary recognition. Moreover, one assistant had access to all cases and generated/reviewed all outputs. Stable history and correct boundaries here therefore cannot establish independent or robust behavior.

The output itself recognizes this in the boundary `contrary_evidence_or_limitations` field. This limitation is retained rather than labeling the test a robust success. There is no manufactured failure and no claim of a before/after performance improvement.

Additional scope limitation: the six-paper packet supports a selected technical lineage, not a comprehensive causal history of agents. Economic, regulatory and older intellectual precursors remain outside the checked evidence.

## Disposition

These three saved responses meet the qualitative criteria in this assistant review and are structurally validated separately. They support review for integration as a bounded Creation specialist. They do not establish production reliability or justify autonomous deployment. No specialist-instruction revision was made: the observed limit is chiefly in test design/evidence coverage, and this consolidation preserves the already-confirmed design. A later separately authorized evaluation should use fresh uncued cases, independent reviewers and repeated runs. This is not represented as completed workshop work.

Candidate-to-candidate attribution remains in `decision_lineage.md`, confirmed by the user. The present walkthrough does not independently rerun all five candidate agents or prove the integrated version is superior to every candidate.
