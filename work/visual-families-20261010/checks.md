# Visual-family skeleton checks

The user's scope update, “先把骨架搭起来,” narrowed this work to the ten-family index and linked skeleton notes. No style entries, prompt fragments, examples, or complete-catalog claims were added.

The source taxonomy is represented by ten bilingual family labels and codes. Each family note states its scope, selection cue, boundary, and existing method owner. The main router and the photography, illustration, and design methods link to the index conditionally. Their existing style tables link to it without replacing their current content. The project index and architecture note record the new reference path.

## Checks

- `quick_validate.py` passed for `skills/oneirloom`, `skills/oneirloom-style-photography`, `skills/oneirloom-style-illustration`, and `skills/oneirloom-style-design`.
- A local-link scan checked 153 links in 21 touched Markdown files. No missing local targets were found. The external taxonomy link was not fetched.
- A structural check found the exact unique code sequence M, P, C, A, G, R, D, S, F, T; all ten family files exist and carry a skeleton-only status; all four skill entries link to the family index.
- `git -c core.whitespace=cr-at-eol diff --check` passed for the allowed tracked paths. A byte-level scan found no trailing spaces or tabs in the 21 checked Markdown files.
- Plain `git diff --check` reported carriage returns as trailing whitespace on changed CRLF lines. The pre-edit copies of the affected files were captured before editing at `J:\Users\yangda01\Temp\oneirloom-visual-families-baseline-eddbc05b64a34c7986783f6c20d5dfbc`; `git ls-files --eol` shows the method and router files already use CRLF. The CR-aware diff check and byte-level scan passed.

No behavior evaluation, installation, packaging, release, or full test suite was run.
