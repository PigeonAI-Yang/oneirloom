# 10. Paper typography

Read the [collection contract](../template.md) before adapting this recipe. It binds the sample slots and the checks below to the current brief and the shared graphic-design SOP.

## Selection conditions

Choose this recipe when the supplied words are the main subject and one selected word deserves a hand-marked emphasis.

## Source observations and uncertainty

The [style crop](images/reference.png) shows a high-contrast serif headline tightly stacked in the upper-left and middle field. Crumpled off-white paper fills the whole frame. A yellow loop surrounds one middle word, and a small crumpled-paper ball sits below the headline toward the left. Small copy uses the lower-right area and footer.

The source creator, date, model, original prompt, and exact font are unknown. "Paper typography" describes the visible relationship between text and paper rather than a source-published title.

Source metadata remains in the [collection reference record](../reference.json).

## Defining mechanism and relational anchors

- Make the paper fill the frame, with no surrounding mockup scene. Let the headline occupy most of the upper and middle type field while leaving a smaller right-side region.
- Stack the supplied headline tightly with a shared left alignment. Its words are the first reading target and remain legible over the folds.
- Draw one narrow accent loop around the chosen word. The loop follows that word's bounds, leaves the letters visible, and remains a stroke rather than a filled highlight.
- Place one small paper ball below the headline toward the left, with a short contact shadow. It echoes the background material at a subordinate scale.
- Keep supplied right-side and footer copy small. Paper relief contributes texture rather than competing with the headline.

## Adaptation map

Map the source's text block to the actual supplied phrase, choosing line breaks for its length and emphasis. Identify the word to circle in the resolved brief. Four lines and the word `room` belong to the sample, so do not force them onto a new phrase.

## Adjustable slots and scoped sample values

| Slot | Archived sample value | Resolve for the current brief |
| --- | --- | --- |
| Headline | `Make` / `room` / `for` / `ideas.` | Exact requested phrase, line breaks, and display scale |
| Highlight | Narrow yellow oval around `room` | Selected word, chosen accent, and fitted loop bounds |
| Type region | Upper-left block across roughly the upper two-thirds | Actual headline extent and clear small-copy region |
| Material | Crumpled off-white sheet and one small paper ball | Current paper treatment and subordinate ball position |
| Small copy | `SAME` / `SPACE` / `NEW` / `THOUGHTS`; `FIELD 10` | Supplied note and footer only |
| Format | Portrait 2:3 | Requested canvas |

The old prompt's approximate five-percent accent area is a sample choice, not a fixed coverage requirement for a differently sized word.

## Construction and handoff

During the SOP layout, fit the exact headline and circle target first. Reserve space below for the small ball and beside the type for any supplied notes. Translate those bounds into the prompt, then add folds whose contrast leaves the words readable.

## Acceptance against the resolved brief

- The exact requested phrase leads the poster with the resolved line breaks and shared left alignment.
- A narrow loop in the chosen accent encloses only the selected word and leaves its letters visible.
- The paper fills the frame and its folds remain subordinate to the type.
- The small paper ball sits in the agreed lower-left region with contact shadow.
- Supplied small copy fits its assigned regions without borrowing the sample's wording.

## Prompt files and historical evidence

- [Archived Chinese sample prompt](prompt.zh.txt)
- [Archived English sample prompt](prompt.en.txt)

One English generation was made with the built-in `image_gen.imagegen` entrypoint using [`submitted.en.txt`](submitted.en.txt) and the supplied style reference. The inspected result is [`images/transfer-01.png`](images/transfer-01.png); its dimensions, visible elements, and prompt deviations are recorded in [`example.json`](example.json).

The Chinese prompt has not been run. Repeatability is unknown because only one English generation was made.
