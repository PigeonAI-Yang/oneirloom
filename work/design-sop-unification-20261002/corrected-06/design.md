# Dream Weaver with opposed views

This correction delivers a design, complete bilingual prompts, and one generated and visually inspected portrait 2:3 poster. The English prompt was submitted unchanged in one built-in `image_gen` call. The initial design specifies two outward-facing views of one creature identity, fragmented at left and continuous at right; the inspection below records the actual result separately.

## Evidence and adaptation

The [06 style crop](../../../skills/oneirloom-style-design/templates/experimental-editorial-posters/06-swiss-sculpture/images/reference.png) supplies two opposed sculpture views, left-side horizontal fragments, a central vertical splice, page-height crop, a cobalt right field, and compact middle-left type. The exact fragment count and whether the original assets were mirrored or independently photographed remain unknown.

The [approved identity image](../../../docs/assets/dream-cocoon/00-approved-reference.png) supplies an oval purple creature, a dark oval front panel with a four-point yellow star, curved ball-ended antennae, a curled appendage, and blue cords holding a crescent. The image is frontal illustration. It does not establish side anatomy, three-dimensional depth, or physical materials.

For this design, give that identity rounded depth and a three-quarter view, then use a mirrored graphic copy to establish the opposed orientation. Both depictions represent the same identity. They form a printed juxtaposition, not a scene with two interacting creatures. The depth, mirroring, realistic materials, crop, and layout positions are creative adaptation choices. The design does not introduce a human nose, mouth, or new anatomy.

## Resolved working brief

The following fields record the initial design and prompt intent. Actual generation evidence is recorded separately below.

| Field | Decision |
| --- | --- |
| Goal and constraints | Transfer 06's opposed-view mechanism to the Dream Weaver creature. Deliver complete portable prompts, with the exact title `DREAM WEAVER` and footer `ONEIRLOOM`. |
| Frame and hierarchy | Portrait 2:3. The combined creature image fills almost the page height. Upper antenna arcs and lower cords cross the frame. Read the opposed views first, the compact headline next, and the footer last. |
| Regions and relationships | The two image backs meet at a central vertical splice. Warm off-white fills the left field. Cobalt fills the right behind the continuous right view. The left headline sits below or beside the left direction cues, on a compact exposed paper area. |
| Subject and transformation | One nonhuman identity appears twice. The left three-quarter view faces left, with a foreshortened indigo star panel turned toward the outer left edge. Its rectangular horizontal bands have staggered alignment. The right three-quarter view faces right, with a foreshortened indigo star panel turned toward the outer right edge, and remains unfragmented. Rounded body depth and the antenna and curled-appendage contours reinforce the directions. |
| Type and copy | Black bold condensed sans-serif headline, `DREAM` above `WEAVER`, compact at middle-left. Smaller `ONEIRLOOM` at lower-left shares the same left alignment. No additional copy is supplied. |
| Palette and material | Gray-lilac short fur, deep-indigo matte fabric panels, antique-gold brass stars and antenna balls, and blue braided cords with a brass crescent where visible. Warm off-white paper, black type, and cobalt remain flat printed areas. |
| Mechanism | Horizontal rectangular cuts fragment only the left view. The vertical splice juxtaposes the two opposed views. It does not join corresponding parts of a single frontal or right-facing body. |
| Acceptance and evidence | Inspect two visible directions, left fragmentation versus right continuity, scale and crop, type clearance, identity, and exact copy. One generated trial has now been visually inspected; its observed matches and title-overlap deviation are recorded below. |

The left view's indigo panel and star remain readable above or beside the headline. The staggered bands preserve its outward direction even where the image is interrupted. The right panel and star remain legible on the right. A symmetric four-point star alone cannot establish orientation; the panel's foreshortening, body depth, and outward contour must show it.

Use multiple horizontal bands without asserting a source fragment count. Any count chosen during composition is a current design choice. Narrow paper edges and shallow contact shadows expose displacement within the left image. The vertical splice remains a separate meeting boundary. Layer order is paper and cobalt field, right image, left image fragments, then type in its reserved paper area.

Crops may omit lower limbs, cord sections, and accessories. Preserve the local star panels and recognizable antenna cues, with the curl or cord-and-crescent relation where visible. Do not shrink both copies to fit every identity part. Do not use type to conceal the left-facing view.

## Acceptance for an actual result

- The image shows two three-quarter views of the same oval nonhuman identity, joined back-to-back at the central vertical splice. The left view faces left and the right view faces right.
- Each panel remains legible toward its outer side. Foreshortening, rounded body depth, and antenna or curl contours show the opposed directions. Merely mirroring the background does not meet this condition.
- Multiple horizontally edged rectangular bands displace the left image. The right image stays continuous. The vertical splice juxtaposes the views instead of suggesting offset continuation of one body.
- The combined image retains page-height scale and the specified crops. The cobalt field remains visible beside the right-facing contour.
- The compact middle-left headline leaves the left view's panel and direction readable. The only text is `DREAM WEAVER` across two lines and the aligned footer `ONEIRLOOM`.
- The recognizable identity survives realistic material translation and cropping. Human facial anatomy is absent, and each copy need not contain every limb or accessory.
- A single frontal or right-facing body with a displaced left edge fails, even if the palette and materials match. So does a composition with two front-facing copies or a hidden left view.

## Deliverables and status

- [Complete Chinese prompt](prompt.zh.txt)
- [Complete English prompt](prompt.en.txt)
- [Change notes and evidence limits](change-notes.md)

Both prompts describe the same resolved design. Keep any future identity and style inputs outside the prompt and assign their roles separately. Historical prompts, generated images, and JSON records remain unchanged. The English prompt has one inspected trial; the Chinese prompt and repeatability remain untested. No underlying model identity, seed, or success rate is established.

## Actual inspection of one generated trial

The [submitted English prompt](submitted.en.txt) is byte-identical to [prompt.en.txt](prompt.en.txt), with SHA-256 `7A1CEE97A630C53638E0464E7F74227C056E330B95446088DDE37F80455BA3DA`. The [generation receipt](generation.json) records one built-in `image_gen` call and the [1024 × 1536 output](output.png), visually inspected on 2026-10-02.

The left star panel is on the outer-left side and the right panel on the outer-right side, with rounded body depth toward the central vertical splice. The left view has staggered horizontal rectangular bands; the right view is continuous. Cobalt remains on the right. Stars, antennae, a curl, cords, and a crescent remain recognizable. The title `DREAM` / `WEAVER` and footer `ONEIRLOOM` are exact.

The title end overlaps pale fur and partly covers the left body instead of staying entirely on exposed paper. The left star panel and outward orientation remain readable. This result supports the visible opposed-view and fragmentation relations, with that type-clearance deviation. It does not establish exact source geometry, repeatability, or the generator's internal view construction. The underlying model is unknown because the tool response did not expose it.
