# AI Sticker Platform Evidence

Evidence-only research notes; not a final production SOP and not platform acceptance. Retrieval date for every source below: 2026-10-02. No images were generated, uploaded, imported, or submitted.

## Source inventory and access status

| ID | Direct official source | Page title | Last updated visible | Access/evidence status |
|---|---|---|---|---|
| L1 | https://creator.line.me/en/guideline/sticker/ | Guidelines - LINE Creators Market (static stickers) | Unknown; no date visible | Full guideline body inspected. |
| L2 | https://creator.line.me/en/guideline/animationsticker/ | Guidelines - LINE Creators Market (animated stickers) | Unknown; no date visible | Opened through the official sticker-guideline navigation; full guideline body inspected. |
| L3 | https://creator.line.me/en/review_guideline/ | Review Guidelines - LINE Creators Market | Unknown; no date visible | Opened through the official review link; sticker and emoji review sections inspected. |
| T1 | https://core.telegram.org/stickers | Telegram Stickers | Unknown; no date visible | Full official platform guide inspected. |
| T2 | https://core.telegram.org/stickers/webm-vp9-encoding | Encoding Video Stickers and Emoji with .WEBM and VP9 | Unknown; no date visible | Official linked encoding and upload guidance inspected. |
| W1 | https://github.com/WhatsApp/stickers | GitHub - WhatsApp/stickers | Unknown; latest commit date not visible in retrieved page | Official Meta/WhatsApp public repository page inspected. |
| W2 | https://github.com/WhatsApp/stickers/blob/main/README.md | stickers/README.md at main - WhatsApp/stickers | Unknown; no file date visible | Current `main` README inspected; describes third-party pack apps and iOS store-review caveat. |
| W3 | https://github.com/WhatsApp/stickers/blob/main/Android/README.md | stickers/Android/README.md at main - WhatsApp/stickers | Unknown; no file date visible | Full Android README inspected; source for the file, pack, metadata, and import details below. |
| W4 | https://github.com/WhatsApp/stickers/blob/main/iOS/README.md | stickers/iOS/README.md at main - WhatsApp/stickers | Unknown | Page was surfaced, but relevant body text could not be extracted; a subsequent line-specific open returned HTTP 503. Endpoint not retried. |
| W5 | https://faq.whatsapp.com/1056840314992666/ | How to create and share custom stickers and sticker packs (WhatsApp Help Center) | Unknown | Official Meta Help Center page redirected to a platform-specific URL but returned no body text. Search-result snippet exposed only 512 x 512 px and 100 KB, so it is not used as full-page evidence. |
| W6 | https://faq.whatsapp.com/639351827594474/?locale=en_US&cms_platform=web | How to use stickers (WhatsApp Help Center) | Unknown | Official Help Center destination returned no body text. |
| D1 | https://support.discord.com/hc/en-us/articles/4402687377815-Tips-for-Sticker-Creators-FAQ | Tips for Sticker Creators FAQ - Discord | May 26, 2022 (article shows “Updated”) | Full creator requirements and transparency guidance inspected. |
| D2 | https://support.discord.com/hc/en-us/articles/4403089981975-Custom-Stickers-FAQ | Custom Stickers FAQ - Discord | October 4, 2025, 02:54 (article shows “Updated”) | Full server upload, permissions, slots, usage, naming, emoji suggestion, and alt-text guidance inspected. |
| S1 | https://slack.com/help/articles/206870177-Add-custom-emoji-and-aliases-to-your-workspace | Add custom emoji and aliases to your workspace - Slack | Unknown; no date visible | Full official workspace emoji guidance inspected. This is custom emoji, not a sticker-set submission system. |

WeChat locator queries executed exactly as assigned: `site:sticker.weixin.qq.com 表情 制作 规范 上传` and `site:weixin.qq.com 表情开放平台 制作规范 GIF PNG 240`. Both returned empty search results. No official WeChat page was located or inspected; search results provide no current specification evidence.

Count: 14 distinct official source URLs inspected or directly attempted (11 yielded substantive body text, W4 yielded only incomplete page access and then HTTP 503, and W5-W6 returned no page body). The two WeChat searches located zero source pages.

## Platform-specific evidence

### LINE Creators Market: static stickers (L1)

- Deliverables: one 240 x 240 px main image; 8, 16, 24, 32, or 40 sticker images, each at most 370 x 320 px; one 96 x 74 px chat-thumbnail icon. The page gives a 1 MB maximum for each listed image.
- All images are PNG, RGB color mode, at least 72 dpi, with even-numbered width and height. Backgrounds must be transparent. A ZIP upload must be at most 60 MB.
- The page recommends about 10 px of margin between the trimmed image and nearby content. The sticker is auto-resized.
- Metadata character limits: title 40, creator 50, description 160, copyright 50. Some Asian-language characters and symbols count as two characters.
- The page recommends everyday conversational use and readily understood expressions/messages/illustrations. It discourages scenery/object-only or poorly visible designs and sets with little variety. This is qualitative platform guidance, not a fixed expression checklist.
- Workflow shown: select the pack count in Manage Stickers; it may be changed before submission. Paid Creators Market stickers require LINE review approval before sale (L3).

### LINE Creators Market: animated stickers (L2)

- Deliverables: one 240 x 240 px main image as APNG in a `.png` file; 8, 16, or 24 animated sticker images; one 96 x 74 px static PNG chat-thumbnail icon. The animated sticker image canvas is within 320 x 270 px, with at least one dimension at least 270 px. All frames must fit the designated dimensions.
- Each animated image may be at most 1 MB; the whole ZIP may be at most 60 MB. Use RGB color space. Backgrounds must be transparent. The small play marker on the chat thumbnail is added by LINE.
- Each animation has 5-20 frames, 1-4 loops, and no more than 4 seconds total playback. Repeated identical frames may be combined by APNG tools; identical content across all frames will not animate. The first APNG frame is the static storefront/shop image.
- Text fields have the same limits as static stickers: title 40, creator 50, description 160, copyright 50 characters, with the same note about character counting.
- No numeric margin rule was stated on this animated page. The page advises trimming non-animated portions from frames.

### LINE review policy (L3)

- Creators can sell only after the Creators Market review process approves the work. The page reserves rejection/removal discretion and notes that treatment may vary by content, distribution region, and creator characteristics.
- Relevant acceptance risks include poor conversational usefulness/visibility, low set variety, misspellings or metadata mismatches, advertising or URLs, references to competing messaging services, rights/portrait/privacy violations, and sensitive or harmful material. Photo-rights documentation may be requested.
- Emoji have a separate review section. These findings concern sale through LINE Creators Market; they do not establish rules for a private LINE chat or another distribution route.

### Telegram: static assets, vector animation, and emoji (T1)

- Static stickers: PNG or WEBP; one side exactly 512 px and the other side 512 px or less. The page gives no static sticker file-size or pack-count cap. A transparent background, white outline, and black shadow are tips, not stated file requirements.
- Static custom emoji are a different deliverable: exactly 100 x 100 px, PNG or WEBP.
- Vector animated stickers and emoji use Telegram `.TGS`, authored through a vector-editor/After Effects/Bodymovin-TG route. Requirements: 512 x 512 px canvas, objects remain within canvas, loop required, duration at most 3 seconds, 60 FPS, and final rendered file at most 64 KB. The guide enumerates unsupported After Effects features; notably it rules out text layers and raster image layers. The page does not state a separate alpha/background rule.
- Telegram custom emoji share the sticker technology but have the separate 100 x 100 px image requirement. Anyone can create custom emoji, while adding and using custom sets is described as a Telegram Premium feature. Adaptive emoji are a separate use case for solid-color icons that inherit text/theme color.
- Users can also make photo stickers in the in-app Sticker Editor. For designed pack assets, the guide points to the `@Stickers` mini app/bot to create/manage packs and publish assets. The pages do not state a pre-publication approval process.

### Telegram: video assets (T1, T2)

- Video stickers: WEBM with VP9; one side exactly 512 px, other side 512 px or less; at most 3 seconds, 30 FPS, and 256 KB; no audio stream. Looping is recommended, not mandatory in the stated video rules.
- Video emoji are separately 100 x 100 px. Background transparency/alpha is not specified on these video pages.
- Workflow: make video in an editor, encode with VP9 (the guide warns that some encoders default to VP8), remove audio, use constant 30 FPS, then publish/manage the pack through `@Stickers`. T2 advises checking the encoded output size and VP9/no-audio settings.

### WhatsApp third-party sticker packs (W1-W6)

Primary usable evidence here is the current official WhatsApp/stickers repository and its Android README. WhatsApp Help Center pages W5-W6 were attempted but supplied no body; do not treat snippets as a substitute for those pages.

- Sticker image requirement in W3: exactly 512 x 512 px, WebP, transparent background. Static images are at most 100 KB; animated images are at most 500 KB. Animated frame duration is at least 8 ms and total animation duration at most 10 seconds. WhatsApp loops the animation and returns to its first frame, so the first frame should show the complete sticker/readable message. No exact margin is specified.
- Contrast against white, black, colored, and patterned chat backgrounds is called out. The recommended white outside stroke is 8 px; it is a visibility recommendation, not a margin specification.
- Pack boundary: each pack contains 3-30 stickers and is either all static or all animated. A third-party app can carry 1-10 packs. Each pack has its own static 96 x 96 px tray icon of at most 50 KB.
- Android `contents.json` metadata includes pack name and publisher (each max 128 characters), a unique identifier under 128 characters, up to 3 emoji tags per sticker, and optional accessibility text (max 125 characters static, 255 animated). These labels describe sticker meaning/content for screen readers; the README recommends US English, present tense, and non-editorial wording.
- Import/distribution boundary: the official design is an Android/iOS app distributed outside WhatsApp. Android users install the separate app, choose a pack, then explicitly add that pack in WhatsApp; the user confirms inside WhatsApp. The Android API exposes pack metadata and sticker bytes via a ContentProvider and launches WhatsApp's add-pack intent. Users add packs individually; no add-all operation. WhatsApp retains the selected pack and reads sticker files from the provider. The app can check only whether its own packs were added, not inspect other apps' packs.
- W1/W2 say the iOS sample demonstrates the import API but is not an App Store-acceptable template; the app should have more functionality than exporting stickers alone. This is an Apple app-review boundary, not a sticker-art dimension change.

### Discord custom server stickers (D1, D2)

- D1 lists static PNG and animated APNG; exact 320 x 320 px; max file size 512 KB; animation up to 60 FPS. It gives no maximum frame count or animation duration.
- Transparency is recommended: save with a transparent background or remove a solid background. The creator guide recommends using as much of the canvas as possible; it gives no numeric margin. Custom stickers may render at different sizes in different surfaces; desktop chat is listed as 160 x 160 dp.
- Discord custom server stickers are distinct from Unicode emoji and from the standard emoji picker. A related Unicode emoji is required for sticker suggestions; a short accessible description is optional in D1 and recommended in D2.
- Workflow/access: server boosting provides slots (5 default; Level 1 adds 10; Level 2 adds 15 for 30 total; Level 3 adds 30 for 60 total). A server owner or a member with Create Expressions permission uploads through Server Settings > Stickers. Sticker management requires desktop or web, not the mobile app. Upload one file at a time with a name and related emoji. A sticker file cannot be replaced in place; delete and upload a new one.
- Server members can use the server's stickers in that server. Nitro users can use them elsewhere on Discord. No central marketplace review process is described in these help pages; the server owner/permissions and Discord Terms/Community Guidelines govern upload/use.

### Slack custom emoji (S1)

- Slack calls these custom emoji, not stickers. Square images under 128 KB with transparent backgrounds “work best”; these are recommendations, not stated hard upload limits. Accepted formats are JPG, PNG, or GIF; GIFs may contain up to 50 frames. The page gives no pixel dimensions, animation duration, or numeric margin rule.
- Workflow: upload and name through the emoji picker on desktop or iOS. It is currently unavailable to create custom emoji from Slack's Android app. By default members but not guests can create emoji; workspace/org owners can restrict permission. Emoji packs are added as packs, and individual items cannot be removed from a pack.

## Evidence limits

- Platform specs differ by asset type and channel. Static sticker files, animated sticker files, custom emoji, sticker tray icons, and chat UI icons are separate deliverables; the numbers above must not be treated as a common cross-platform preset.
- WeChat remains a source gap: the two assigned official-domain searches returned no result. No numeric rule, file type, or current review policy can be asserted from this evidence.
- WhatsApp's current Help Center content was not readable through the official page route: one page redirected with an empty body, a second did the same, and the GitHub iOS README follow-up returned HTTP 503. W3 supplies usable repository guidance; the unavailable Meta Help Center page is not claimed as verified.
- LINE and Telegram pages did not show an update date. Slack's page did not show an update date. Discord shows the dates recorded above.
- This is source evidence only. No production file was generated, tested against app import, or submitted for platform review.
