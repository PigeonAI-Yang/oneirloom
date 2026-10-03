# Oneirloom static platform profiles

These five profiles apply the 2026-10-02 official-source reading to DreamWeaver artwork. Four profiles contain verified source requirements. The WeChat profile remains pending. Source verification does not establish successful generation, import, upload, or platform acceptance.

The profiles preserve the [brand identity](oneirloom-brand.md). They use the same reaction artwork with platform-specific exports. Dimensions are pixels. A value absent from the cited page remains unknown; absence does not mean unlimited. Production compliance depends on the selected route's current official rules.

## LINE static stickers

Source: [LINE Creators Market static sticker guidelines](https://creator.line.me/en/guideline/sticker/), relevant body read on 2026-10-02. This profile covers ordinary static stickers, not custom-caption, message, animated, or sponsored stickers.

| Output | Hard requirements | Oneirloom file and composition |
| --- | --- | --- |
| Individual reactions | PNG with transparent background; maximum 370 × 320; each image at most 1 MB | `oneirloom-line-static/01.png` contains a complete DreamWeaver reaction, such as a compact acknowledgment with four grips and the crescent secured. An exact caption can share the canvas if legible. |
| Pack main image | One PNG with transparent background, 240 × 240; at most 1 MB | `oneirloom-line-static/main.png` identifies the collection with the front mascot. A short brand lockup is optional if it survives this size. |
| Chat thumbnail | One PNG with transparent background, 96 × 74; at most 1 MB | `oneirloom-line-static/tab.png` gives the picker a recognizable mascot silhouette. It is a separate composition, not a scaled contact sheet. |
| Pack archive | 8, 16, 24, 32, or 40 reaction images; ZIP at most 60 MB | `oneirloom-line-static.zip` contains the selected count plus the two required identification assets. |

The official page recommends about 10 pixels of margin around trimmed artwork. This is margin guidance, not an additional canvas size or a hard alpha-border rule. The named file layout is a local packaging convention informed by the source/export workflow.

Before delivery, count the reaction files separately from `main.png` and `tab.png`. Check the actual dimensions, PNG encoding, alpha, image sizes, and ZIP size. Inspect the antenna balls, tail, all four grips, and crescent against light and dark chat backgrounds. The [daily sixteen](../templates/daily-sixteen/template.md) and [eight-slot workspace](../templates/eight-slot-workspace/template.md) fit selectable LINE counts; that arithmetic does not prove image compliance.

## Telegram static stickers

Source: [Telegram static stickers](https://core.telegram.org/stickers), static subsection read on 2026-10-02. This profile excludes animated stickers, video stickers, and custom emoji.

| Output | Verified rule or evidence limit | Oneirloom file and composition |
| --- | --- | --- |
| Individual reactions | PNG or WebP; one side exactly 512 and the other side at most 512 | `oneirloom-telegram-static/01-acknowledge.png`, preferably a square composition when it accommodates the net and antennae |
| Alpha and outline | Transparent background, white stroke, and black shadow are tips in the read guide, not stated hard requirements | Transparent artwork is the local default. Add an outside stroke only if the actual dark outline loses visibility on chat backgrounds. |
| File cap and pack count | No static file-size cap or pack-count cap stated in the read subsection | Neither value is assumed unlimited. The selected import route must settle any outstanding limit before a compliance claim. |
| Separate pack icon | No separate main image or icon specified in the read subsection | `oneirloom-telegram-static/preview.png` may show the collection with the lockup for local review. It is not a required upload asset or one of the reaction files. |

Before delivery, verify the exact-side rule and the actual PNG or WebP encoding. Check the chosen alpha treatment and every reaction at chat size. Preserve the unresolved cap and count status instead of copying another platform's limits. The [ten reactions](../templates/ten-reactions/template.md) is one possible collection, not a Telegram-mandated count.

## WhatsApp Android static stickers

Sources: [WhatsApp stickers repository](https://github.com/WhatsApp/stickers/blob/main/README.md) establishes the third-party app route; the [Android README](https://github.com/WhatsApp/stickers/blob/main/Android/README.md) supplies the requirements below. Both relevant bodies were read on 2026-10-02. This profile does not establish the in-app creator's rules or iOS app-store acceptance.

| Output | Hard requirements | Oneirloom file and composition |
| --- | --- | --- |
| Individual reactions | Exactly 512 × 512; WebP; transparent background; static file at most 100 KB | `oneirloom-whatsapp-android-static/01-acknowledge.webp` holds one DreamWeaver reaction with complete antennae, tail, grips, and net. |
| Sticker-picker tray icon | Separate static image, exactly 96 × 96; at most 50 KB | `oneirloom-whatsapp-android-static/tray.png` uses the front mascot for collection recognition. The inspected evidence does not establish an icon-format rule; this filename is a local choice to verify with the implementation. |
| Pack and app counts | Each pack contains 3–30 stickers; one Android app contains 1–10 packs; static and animated stickers cannot mix in one pack | `oneirloom-whatsapp-android-static/` contains one selected static pack. This directory alone is not an Android integration. |

The README recommends an 8-pixel outside white stroke. The stroke is not padding and is not a hard requirement. Its purpose is visibility on varied backgrounds. The tray icon usually omits the wordmark at this size. A separate local `preview.png` can carry the wordmark and reaction labels without becoming an import asset.

Before delivery, inspect actual WebP encoding, transparency, 512-square canvases, file sizes, the tray icon, and the pack count. Check dark outlines and thin blue net strands after compression. Android packaging, metadata, and import need their own actual implementation evidence. The [soft six](../templates/soft-six/template.md) supplies a possible six-item collection, not an app or a verified import.

## Discord server static stickers

Sources: [Tips for Sticker Creators FAQ](https://support.discord.com/hc/en-us/articles/4402687377815-Tips-for-Sticker-Creators-FAQ) supplies the artwork rules. The [Custom Stickers FAQ](https://support.discord.com/hc/en-us/articles/4403089981975-Custom-Stickers-FAQ) supplies upload context. Both bodies were read on 2026-10-02.

| Output | Verified rule or evidence limit | Oneirloom file and composition |
| --- | --- | --- |
| Individual server stickers | Exactly 320 × 320; PNG for static images; at most 512 KB per file | `oneirloom-discord-static/01-acknowledge.png` contains one reaction. Keep the star, net, and gold crescent visible after reduction. |
| Transparency | Recommended by the creator tips, not stated as a hard requirement | Transparent artwork is the local default. Inspect the edges on Discord's relevant light and dark backgrounds. |
| Pack count | No fixed pack count stated in the creator tips | Available server slots constrain upload capacity. They are not a required reaction inventory or pack size. |
| Cover or tray icon | No separate pack or tray image stated in the read creator tips | `oneirloom-discord-static/preview.png` is an optional local contact sheet with a brand header. It is not a required server upload. |

The tips recommend using as much canvas space as possible but state no numerical margin. Preserve room for the antennae and net rather than enlarging until they clip. The supporting FAQ describes selecting a related Unicode emoji and recommends concise alt text. Those fields aid discovery and accessibility; they do not alter the artwork's size rule.

Before delivery, check exact dimensions, PNG encoding, and file size. Inspect the reduced reaction and any caption. Record the matching emoji and a concise description when preparing upload metadata. Server permissions, capacity, and actual upload remain separate observations. The [seven poses](../templates/seven-poses/template.md) is a design collection whose uploadability depends on the target server's available capacity.

## WeChat static stickers, pending official requirements

Source: [WeChat making-specifications entry](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html#/makingSpecifications), attempted on 2026-10-02. The result had no readable official body. Status: SOURCE GAP. The cause is unknown; no login requirement is inferred.

| Planned output | Current status | Oneirloom working file and composition |
| --- | --- | --- |
| Individual reactions | Canvas size, file format, alpha requirement, file cap, and pack count remain unverified | `oneirloom-wechat-pending/source/01-acknowledge.svg` can retain editable local artwork on a 1024 × 1024 working canvas. This is a local design choice, not a verified WeChat export size or required source format. |
| Collection identification image | Required role, size, encoding, and count remain unverified | `oneirloom-wechat-pending/source/cover-draft.svg` can place the front mascot above the brand lockup for design review. It is provisional, not a confirmed submission asset. |
| Picker icon | Whether this asset is required, and its specifications, remain unverified | `oneirloom-wechat-pending/source/icon-draft.svg` can explore a compact mascot composition. It is provisional. |
| Preview | Local review only | `oneirloom-wechat-pending/preview.png` can compare the selected reactions and exact captions. It is not an accepted platform file. |

The `.svg` examples apply when the chosen production path actually creates editable vector artwork. They do not describe the supplied raster reference as a vector file. An editable raster source is also suitable for local design work.

Before a WeChat export claim, obtain the readable official requirements for the exact submission route, then set the real export dimensions, encoding, alpha, caps, counts, and required identification assets. No remembered 240-pixel or 500-KB value fills this gap. The gap does not block original reaction planning, editable artwork, or a clearly labeled local preview. The [chat coverage](../templates/chat-coverage/template.md) can organize that design work without importing platform counts.
