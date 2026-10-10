# Prompt-delivery closure acceptance record

This report records the initial C1 closure batch and the separately sourced C2 rerun. It preserves the first failure even though the single corrected-case rerun passed.

## Results

The initial batch contains 10 native-child JSON receipts and 16 actual turns. The Primary verdict covered 13 scoped cases: 12 passed, 1 failed, and 0 were unexecuted. The C1 interaction-contract SHA-256 recorded by every initial receipt is 146d2abce476fc525e5b2086fc0a5866a028cd0ad5c95f0e519531f03e579ac1.

A fresh single-case rerun used C2 interaction-contract SHA-256 13dc08d40afff785d96f0e6855f23981d4ba047d619beb3072cef33810b23449. The C2 author receipt confirms one exact sentence replacement and that all other source bytes remained unchanged. The Primary verdict for that rerun is passed. Latest scoped coverage is 13 passes, 0 failures, and 0 unexecuted cases, combining the 12 C1 passes and one C2 rerun. The other 12 cases were not rerun on C2; this does not establish repeatability.

| Case | Actual source turns | C1 verdict | Latest verdict | Evidence / reason |
| --- | --- | --- | --- | --- |
| clear-breakfast-direct | closure-clear, turn 1 | Passed | Passed | Proceeds without renewed consultation; complete fenced Chinese prompt retains one intact oval bread, three shallow scores, unspecified white powder and exact supplied title. |
| vague-bread-followup | closure-vague, turns 1–2 | Passed | Passed | Two consequential questions and three different mechanisms precede the actual choice; the second turn delivers the selected miniature station with its literal title, independent fantasy scenery and no unsupported-fact inventory. |
| diagnose-package-structure | closure-package, turn 1 | Passed | Passed | Labels deviations as user-reported, leaves execution causes unresolved, and restores one whole bread in a transparent soft bag with left fold and upper-right label in a complete fenced correction. |
| blurred-label-unknown-filling | closure-package, turn 2 | Passed | Passed | Declares exact brand text unavailable, does not guess it, and explicitly keeps the requested brand-accurate final image incomplete while preserving independent subject/layout work. |
| no-search-no-result | closure-no-search, turn 1 | Passed | Passed | Discloses no competitor research or inspected image; proceeds with the supplied warm-breakfast direction and complete prompt, using the title as the only text instead of a prohibited-claims list. |
| confirmed-chocolate-architecture | closure-chocolate, turn 1 | Passed | Passed | Attributes the ingredient to the supplied manufacturer-sheet description, uses chocolate as imaginary architectural material and keeps the rectangular packaged bar prominent without invented brand details. |
| critical-material-conflict | closure-conflict, turn 1 | Passed | Passed | Names packaging, shape and count conflicts between two uninspected descriptions, asks which current item to use and continues independent background/layout choices. |
| doubao-portable-language | closure-doubao, turn 1 | Passed | Passed | Separates assistant instructions from complete Chinese/English image prompts; preserves literal Chinese title in both, reference guidance outside blocks and no native-installation or unverified-control claim. |
| research-denial-local-progress | closure-denial, turn 1 | Passed | Passed | Treats supplied access denial as a stop, reports no retry or invented findings, and continues with three product-grounded directions and complete Chinese prompts. |
| sequential-background-style-copy | closure-local-edits, turns 1–3 | Passed | Passed | Across three actual turns, updates wall then medium then exact title while retaining one intact bread, scores, object placement and other current choices; each revision is a full fenced prompt. |
| reject-old-direction | closure-local-edits, turn 4 | Passed | Passed | Replaces the rejected illustrated breakfast scene with a centered dark-gray product photograph while retaining supported bread facts and omitting old props/copy. |
| realistic-and-miniature | closure-truth, turn 1 | Passed | Passed | Delivers two complete prompts with the same supported exterior; factory facilities are clearly imaginary scenery rather than filling or real-production evidence. |
| ingredient-claim-fallback | closure-truth, turn 2; closure-ingredient-final, turn 1 | Failed | Passed | C1 correctly rejected unsupported strawberry/health facts but exported an unknown-fact list; C2 instead uses closed decorative-liquid pipes on a separate platform, suggested replacement copy and a complete fenced prompt without that inventory. |

The saved C1 answer for ingredient-claim-fallback is preserved verbatim, including the failed generation-block wording “不呈现商品馅料、配料或营养信息”. The C2 answer explains the unsupported filling and nutrition claim outside the prompt and presents the decorative liquid in closed pipes on a separate acrylic platform, with visible separation from the intact bread. The corrected answer is a single fresh case result, not evidence that all cases pass repeatedly.

Specific visible exclusions remain valid when they describe a requested image constraint, such as no copy or no tableware. No lexical ban on negation was applied. The no-search case's saved answer includes “标题为画面唯一文字”; that excerpt belongs to closure-no-search and is separate from the two suggested text lines in the C2 ingredient answer.

## Source and execution limits

All 10 initial receipts recorded an explicit read of the shared interaction contract at C1. The final single-case receipt records C2, and the current source hash matches that recorded C2 hash. Each actual-answer input and answer is copied verbatim to [closure-actual-answers.md](closure-actual-answers.md); the original per-run records remain linked there and unchanged.

Each child request recorded gpt-6-luna at max, and the host field identifies a native child with explicit source reads. The server response model was not observed. These receipts establish explicit source reads from the checkout, not installed-skill discovery or production-entry behavior.

The denial and local-edit receipts record static ecommerce example references among the material read by those sessions. Their inclusion is preserved in the raw read records; they are not treated as prior runtime behavior or evaluation-expectation evidence. The independent structural receipt [closure-structure-checks.json](closure-structure-checks.json) records 18 passes at its C1 snapshot. It was not rerun after C2 and is not behavior evidence. The existing 60 evaluation fixtures were left intact. The missing scripts/check_skills.py runner was not recreated or repaired.

No image generation, actual image review, installation, deployment, or publication was performed. No image-level or repeatability claim is made.

## Receipt links

- Initial C1 turn and answer copies: [closure-actual-answers.md](closure-actual-answers.md)
- Single C2 actual run: [closure-ingredient-final.json](closure-ingredient-final.json)
- C2 source author check: [closure-inventory-author-checks.json](closure-inventory-author-checks.json)
- Static source-structure receipt: [closure-structure-checks.json](closure-structure-checks.json)
- Machine-readable per-case results and source read hashes: [closure-behavior-checks.json](closure-behavior-checks.json)
