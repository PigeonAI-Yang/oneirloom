# OpenAI plugin submission preparation

This is a skills-only package candidate. It has no MCP server, connected account, reviewer credentials, or custom UI. This document prepares the manual publisher steps; no portal upload, identity verification, attestation, submission, or publication was performed.

## Package facts

- Plugin: `oneirloom`, version `0.1.1`, category `Productivity`.
- Contents: 15 skills, the `assets/icon.svg` listing icon, package documentation, and third-party notices.
- Source snapshot: `8d195d4fc9404d5da71733c861fd947aa109d4f1`.
- Corrected native install and discovery: the local 0.1.1 candidate was enabled on Codex CLI 0.153.0. Its 117 ZIP entries matched the extracted package and installed cache by hash and size; eight Git LFS objects were hydrated, no pointers remained, and all 25 raster images decoded. `skills/list` returned all 15 skills with zero candidate-specific errors. A separate local-wrapper install of public commit `463e68f1a4965b7bedba68d2946b93cb743874bb` matched all 343 source files to the cache and discovered all 15 skills with zero candidate-specific errors. The direct GitHub shorthand remains untested. The final documentation update leaves all skill files, scripts, plugin manifests, icons, and images unchanged from the tested package. The optional renderer passed a separate local synthetic-image check; see [compatibility](COMPATIBILITY.md).
- Public repository and marketplace: published. OpenAI plugin directory: not submitted or listed.
- Website and privacy-policy URLs: live reachability and content checks passed on 2026-10-02 for all six Chinese and English product, installation, and safety pages. See [compatibility](COMPATIBILITY.md) for the verification scope and canonical destinations.

## Publisher actions

1. Confirm the organization and project that will own the plugin. An organization owner can submit; other members need Apps Management Write.
2. Complete the required individual or business developer verification in [organization settings](https://platform.openai.com/settings/organization/general).
3. Review `THIRD_PARTY_NOTICES.md`, the bundled Qwen research-license text and Notice, and provenance/redistribution rights for every bundled third-party asset and example. Resolve any rights gap before submission.
4. Review the public listing copy, package contents, and publisher identity. The website and privacy-policy URLs have passed live checks. Recheck the public URLs if they change, including the support destination.
5. Open [Plugins](https://platform.openai.com/plugins), select your verified developer identity, and upload `dist-plugin/oneirloom-0.1.1.zip` as a skills-only package. Keep credentials and private data outside the ZIP.
6. Wait for the metadata and skill scans. Copy the portal findings, resolve required issues in the source package, create a corrected ZIP, and upload it again.
7. Review the final draft and complete only the policy attestations the publisher can truthfully make. Submit for review; publish only after approval and the publisher's explicit release decision.

Skills-only submissions do not require MCP positive/negative test cases or an MCP walkthrough video. Skill scans and developer verification still apply. No portal scan or review result is available for this candidate.

## English listing copy

- **Display name:** `Oneirloom · 织梦师`
- **Short description:** `Turn visual ideas into prompts`
- **Long description:** `Oneirloom bundles 15 skills for turning visual ideas into image prompts, analyzing references, shaping composition and light, adapting writing guidance for Krea 2 and Qwen-Image-2.1, and diagnosing results. A host with image input is needed for visual analysis. Prompts do not generate images; generation requires a separately available model or tool and is not guaranteed. The optional prompt-card renderer requires local Python, Pillow, Playwright, a browser, and file access. No MCP server, account connection, background service, or automatic upload is bundled.`

## 简体中文本地化文案

以下中文文案可用于本地化字段；提交入口是否提供对应语言字段仍需发布者核实。

- **显示名称：** `Oneirloom · 织梦师`
- **简短描述：** `把视觉想法变成图像提示词`
- **详细描述：** `Oneirloom 提供 15 个视觉创作技能，帮助拆解参考图、描述构图与光线、编写图像提示词，并复盘生成结果。参考图分析需要支持图像输入的宿主。提示词本身不会生成图片；实际生成需另行提供模型或工具，且结果无法保证。可选提示卡渲染器需要本地 Python、Pillow、Playwright、浏览器和文件访问权限。插件不包含 MCP 服务、账号连接、后台服务或自动上传。`

## Official references

- Package format: https://developers.openai.com/plugins/build/plugins
- Upload and submit: https://developers.openai.com/plugins/deploy/submission
- Submission errors: https://developers.openai.com/plugins/deploy/submission-errors
- Plugin guidelines: https://developers.openai.com/plugins/plugin-guidelines
- Codex skills: https://developers.openai.com/codex/skills/
