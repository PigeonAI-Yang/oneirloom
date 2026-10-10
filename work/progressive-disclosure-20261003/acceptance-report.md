# Actual-source text acceptance

This report assembles the seven read-only execution receipts and the Primary-approved case verdicts. The exact saved turn inputs and answers are in [actual-answers.md](actual-answers.md).

## Evidence and scope

- All 7 assigned JSON receipts parse. They contain 14 real turns; all 14 input fields and all 14 saved answer fields are preserved verbatim in [actual-answers.md](actual-answers.md).
- Source hash records: 53 rows, 49 match and 4 differ. The 8 distinct source `SKILL.md` files account for 27 recorded rows; all match. The 2 source project documents, 2 host documents, and 4 source references are counted separately.
- The four differing rows all name `J:\PigeonYang\skills\oneirloom\PROJECT-FILES.md`: receipt SHA-256 `1294F0C02CA4B79E44A0AB7B4A735C415524B320311073182F83D06FFD9A2DFB`; assembly-check raw SHA-256 `994DF4B63CA8BEE300D75943EC2FA173F274B47C597E7C539B1B2A53E33EBE67`. The independent structural record lists the earlier `1294F0...` fingerprint and reports a later status modification without rechecking its contents. This index change is recorded separately and is not counted as a `SKILL.md` mismatch; no final-current index hash or publication claim is made. Receipt paths were preserved; repeated separators were normalized only when resolving current files.
- Independent structural receipts are available in [structure-checks.json](structure-checks.json) and [structure-notes.md](structure-notes.md). The notes state: “Static checks against pinned source `d5df2ed` passed for 18 skill bodies, unchanged public names, 18 explicit shared-contract links, all 33 manifest files, 183 resolvable local links, balanced fences, and zero active references to the retired graphic SOP”; “quick_validate.py passed all 18 entries”; and “Both path-scoped `git diff --check` commands returned 0 with no output.” The same notes say: “No structural suite was rerun after the transition.” Checks ran at `b6397ec`; finalization later observed `f8059e1`, with no pretransition per-file fingerprints, so this evidence has a snapshot gap and is not a current runtime check.
- Evidence is from native child sessions that read the shared source checkout. The Primary dispatch requested `gpt-6-luna` at `max`; some saved records have `requested_model: null` or no exposed model identity, so only the requested model is established here. The server response model is unknown.
- Installed skill discovery and production-entry behavior were not verified. These are text-turn outcomes; image generation/viewing and visual acceptance were not performed. The original `scripts/check_skills.py` is absent per the supplied task evidence; the stale cached checker was not rerun or repaired.
- The current source is a local migration with known behavior gaps. This assignment did not commit, push, install, deploy, or run paid generation. No publication or installed-copy claim is made.

## Primary-approved verdicts for the 13 appended ecommerce cases

Scope is the combined case plus shared prompt-contract requirement. Counts are 6 passed, 3 failed, and 4 unexecuted. Earlier passes are not carried forward as current.

- **PASSED — `clear-breakfast-direct`.** Immediate complete Chinese target; retains the known powder without assigning an ingredient; read only the coordinator, shared contract, product, design and photography instructions for this prompt task.
  Input: [actual-answers.md#clear-breakfast-turn-1-input](actual-answers.md#clear-breakfast-turn-1-input)
  Saved actual answer: [actual-answers.md#clear-breakfast-turn-1-actual-answer](actual-answers.md#clear-breakfast-turn-1-actual-answer)
- **PASSED — `blurred-label-unknown-filling`.** Turn 2 declares exact brand text unmet, requests reliable evidence, and continues with a nonfinal layout without a silent substitute.
  Input: [actual-answers.md#package-miss-dialogue-turn-2-input](actual-answers.md#package-miss-dialogue-turn-2-input)
  Saved actual answer: [actual-answers.md#package-miss-dialogue-turn-2-actual-answer](actual-answers.md#package-miss-dialogue-turn-2-actual-answer)
- **PASSED — `realistic-and-miniature`.** Turn 1 provides two complete prompts using the same supported exterior; the factory scene is fantasy scenery.
  Input: [actual-answers.md#truth-creative-dialogue-turn-1-input](actual-answers.md#truth-creative-dialogue-turn-1-input)
  Saved actual answer: [actual-answers.md#truth-creative-dialogue-turn-1-actual-answer](actual-answers.md#truth-creative-dialogue-turn-1-actual-answer)
- **PASSED — `ingredient-claim-fallback`.** Turn 2 rejects unsupported filling and health implications, then gives usable fantasy scenery.
  Input: [actual-answers.md#truth-creative-dialogue-turn-2-input](actual-answers.md#truth-creative-dialogue-turn-2-input)
  Saved actual answer: [actual-answers.md#truth-creative-dialogue-turn-2-actual-answer](actual-answers.md#truth-creative-dialogue-turn-2-actual-answer)
- **PASSED — `sequential-background-style-copy`.** Local turns 1–3 retain facts and unrelated choices, with full blocks in all three saved answers.
  Inputs / saved answers: [actual-answers.md#local-edits-dialogue-turn-1-input](actual-answers.md#local-edits-dialogue-turn-1-input) / [actual-answers.md#local-edits-dialogue-turn-1-actual-answer](actual-answers.md#local-edits-dialogue-turn-1-actual-answer); [actual-answers.md#local-edits-dialogue-turn-2-input](actual-answers.md#local-edits-dialogue-turn-2-input) / [actual-answers.md#local-edits-dialogue-turn-2-actual-answer](actual-answers.md#local-edits-dialogue-turn-2-actual-answer); [actual-answers.md#local-edits-dialogue-turn-3-input](actual-answers.md#local-edits-dialogue-turn-3-input) / [actual-answers.md#local-edits-dialogue-turn-3-actual-answer](actual-answers.md#local-edits-dialogue-turn-3-actual-answer)
- **PASSED — `reject-old-direction`.** Turn 4 replaces illustration, blue-wall, props, and copy direction with dark-gray photography while retaining bread facts.
  Input: [actual-answers.md#local-edits-dialogue-turn-4-input](actual-answers.md#local-edits-dialogue-turn-4-input)
  Saved actual answer: [actual-answers.md#local-edits-dialogue-turn-4-actual-answer](actual-answers.md#local-edits-dialogue-turn-4-actual-answer)
- **FAILED — `vague-bread-followup`.** Guidance, direction choice, and unknown-fact behavior passed; turn 2 adds only D/F. The final prompt exports the prohibition checklist “不添加品牌、价格、卖点、配料、额外标语或水印”, contrary to the positive concrete internal-checks rule.
  Inputs / saved answers: [actual-answers.md#vague-dialogue-turn-1-input](actual-answers.md#vague-dialogue-turn-1-input) / [actual-answers.md#vague-dialogue-turn-1-actual-answer](actual-answers.md#vague-dialogue-turn-1-actual-answer); [actual-answers.md#vague-dialogue-turn-2-input](actual-answers.md#vague-dialogue-turn-2-input) / [actual-answers.md#vague-dialogue-turn-2-actual-answer](actual-answers.md#vague-dialogue-turn-2-actual-answer)
  Preserved sub-behaviors: Guidance/direction/unknown-fact behavior passed.; Turn 2 adds only D/F.
  Presentation record: Turn 1 explored directions and did not require a generation prompt. The saved turn-2 answer is unfenced; a later assistant final is reported to have added code fences around the same turn-2 text. The saved transcript is unchanged here, and exact-final matching is not claimed.
- **FAILED — `diagnose-package-structure`.** Fact, count, and package-attribution behavior passed, but the saved correction lacks the required separate copyable block.
  Input: [actual-answers.md#package-miss-dialogue-turn-1-input](actual-answers.md#package-miss-dialogue-turn-1-input)
  Saved actual answer: [actual-answers.md#package-miss-dialogue-turn-1-actual-answer](actual-answers.md#package-miss-dialogue-turn-1-actual-answer)
  Preserved sub-behaviors: Fact/count/package attribution behavior passed.
  Presentation record: The first saved response has no code block; the later final merely pointed to the receipt.
- **FAILED — `no-search-no-result`.** Research and inspection honesty passed, but the prompt exports the long internal negative checklist “不添加未提供的品牌、价格、折扣、销量、配料、产地、功效或产品卖点”, stacking negatives.
  Input: [actual-answers.md#no-search-turn-1-input](actual-answers.md#no-search-turn-1-input)
  Saved actual answer: [actual-answers.md#no-search-turn-1-actual-answer](actual-answers.md#no-search-turn-1-actual-answer)
  Preserved sub-behaviors: Research/inspection honesty passed.
- **UNEXECUTED — `confirmed-chocolate-architecture`.** No current execution input or answer is present in the seven completed receipts; no earlier pass is carried forward.
- **UNEXECUTED — `critical-material-conflict`.** No current execution input or answer is present in the seven completed receipts; no earlier pass is carried forward.
- **UNEXECUTED — `doubao-portable-language`.** No current execution input or answer is present in the seven completed receipts; no earlier pass is carried forward.
- **UNEXECUTED — `research-denial-local-progress`.** No current execution input or answer is present in the seven completed receipts; no earlier pass is carried forward.

## Additional nonproduct text cases

- **PASS — nonproduct turn 1.** Scoped text outcome: prompt-only original poster request; no image inspection was needed or claimed.
  Input: [actual-answers.md#nonproduct-graphic-dialogue-turn-1-input](actual-answers.md#nonproduct-graphic-dialogue-turn-1-input)
  Saved actual answer: [actual-answers.md#nonproduct-graphic-dialogue-turn-1-actual-answer](actual-answers.md#nonproduct-graphic-dialogue-turn-1-actual-answer)
- **PASS — nonproduct turn 2.** Scoped text outcome: source analysis was triggered by the supplied layout description; no image-reference inspection is claimed.
  Input: [actual-answers.md#nonproduct-graphic-dialogue-turn-2-input](actual-answers.md#nonproduct-graphic-dialogue-turn-2-input)
  Saved actual answer: [actual-answers.md#nonproduct-graphic-dialogue-turn-2-actual-answer](actual-answers.md#nonproduct-graphic-dialogue-turn-2-actual-answer)

## Test-harness notes

- The nonproduct receipt records a failed startup attempt at `J:\PigeonYang\skills\oneirloom\SKILL.md`; the correct direct entry was `skills\oneirloom\SKILL.md` and is present in its source-read records. This is the recorded harness path error, not evidence of a source failure.
- The extra local-edits worktree receipt is preserved as harness evidence; it is not treated as a source failure.
- For `vague-bread-followup`, the saved turn-2 answer remains unfenced even though a later assistant final is reported to have added code fences around the same text. This report does not alter the saved transcript or claim exact-final matching.
- For `diagnose-package-structure`, the saved first response contains no separate code block and the later final merely pointed to the receipt; this is recorded as a presentation/delivery failure while preserving the approved fact, count, and package-attribution sub-behaviors.

Final snapshot closure: [final-delivery-checks.json](final-delivery-checks.json) records before/after HEADs and current fingerprints for all 33 manifest files. The current map differs from the earlier structural fingerprint map only at the three previously identified status-update paths; its 33-file content hash was unchanged across this closure. The current validator passed 18/18 skills, all 18 skills link to the shared interaction contract, the retired graphic SOP path is absent, and local links/fences pass for the three current documents, this report, and `actual-answers.md`. The saved answers remain unchanged with 14 input and 14 answer headings, and the 13 ecommerce verdicts remain 6 passed, 3 failed, and 4 unexecuted. The earlier `b6397ec` snapshot limitation remains as recorded; this closure identifies current content and does not claim a rerun of that earlier structural check.
