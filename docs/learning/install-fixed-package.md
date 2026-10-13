---
article_id: oneirloom.learning.install-fixed-package
version: fixed-0.3.0-preview.1-1
date: 2026-10-12
locale: zh-CN
title_zh: "安装已发布的固定包"
title_en: "Install the published fixed package"
sources:
  - "[当前固定包发布记录](../releases/0.3.0-preview.1-publication.md)"
  - "[历史 18 技能固定包记录](../releases/0.2.0-preview.1-publication.md)"
evidence: "Authored guidance; no image rendered; no new installed behavior claim."
---

# 安装已发布的固定包

本路径安装已经发布的 `0.3.0-preview.1` 固定包，包含 22 个同级技能目录。下载发布者提供的 ZIP，核对校验值和包内 `SOURCE-MANIFEST.json`，再复制到你的 Codex 项目；GitHub 自动生成的源码 ZIP 不是本路径使用的安装包。

## 下载并核对发布文件

从 [0.3.0-preview.1 发布页](https://github.com/PigeonAI-Yang/oneirloom/releases/tag/v0.3.0-preview.1)下载 [oneirloom-0.3.0-preview.1.zip](https://github.com/PigeonAI-Yang/oneirloom/releases/download/v0.3.0-preview.1/oneirloom-0.3.0-preview.1.zip) 和 [SHA256SUMS.txt](https://github.com/PigeonAI-Yang/oneirloom/releases/download/v0.3.0-preview.1/SHA256SUMS.txt)。这份固定 ZIP 的大小为 **104,816,216 字节**，SHA-256 为：

```text
738ff6ded83f060bcb3dd226f194cfa8f03ad1c18086faf3bfdc49c0743f7743
```

在下载目录运行以下命令，将结果与校验文件里**同名 ZIP**的条目及上面的值比较：

```powershell
Get-Item -LiteralPath './oneirloom-0.3.0-preview.1.zip' | Select-Object Name, Length
Get-FileHash -Algorithm SHA256 -LiteralPath './oneirloom-0.3.0-preview.1.zip'
```

校验一致后，解压到一个新目录，找到同时含有 `skills/` 和 `SOURCE-MANIFEST.json` 的包根目录。在该目录核对 manifest：

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath './SOURCE-MANIFEST.json'
$oneirloomManifest = Get-Content -Raw -LiteralPath './SOURCE-MANIFEST.json' | ConvertFrom-Json
$oneirloomManifest.package.version
$oneirloomManifest.skillIds.Count
$oneirloomManifest.skillIds
```

manifest 的 SHA-256 应为 `3148d84269ce32f974105db7613e3c30d99429961c1f43dd4d59217be79c9d88`，包版本为 `0.3.0-preview.1`，`skillIds` 有 22 项。目录清单如下；以这份固定包的 manifest 逐项对照，不混入开发源文件：

```text
oneirloom
oneirloom-brand-identity
oneirloom-camera-composition
oneirloom-character-sheet
oneirloom-color-light
oneirloom-craft-construction
oneirloom-digital-form
oneirloom-dream-weaving
oneirloom-expression-stickers
oneirloom-figure-art
oneirloom-icon-design
oneirloom-image-tutorial
oneirloom-model-krea-2
oneirloom-model-qwen-image-2-1
oneirloom-product-art-direction
oneirloom-prompt-card
oneirloom-result-diagnosis
oneirloom-space-conception
oneirloom-style-design
oneirloom-style-illustration
oneirloom-style-photography
oneirloom-visual-analysis
```

## 安装到一个新的 Codex 项目

1. 创建一个空白项目目录，在其中准备 `.agents/skills/`。如果你要升级现有项目，先备份该安装原有的 Oneirloom 目录、本地修改、manifest 和已知可用包，记录它们的版本及校验值。保留其他技能和来源不明的目录；没有备份时，不直接覆盖。
2. 把固定包 `skills/` 中 manifest 列出的 **22 个完整同级目录**复制到项目的 `.agents/skills/`，保留目录名和内部文件。不要再套一层 `oneirloom/`，也不要只复制各目录的 `SKILL.md`。
3. 逐项核对项目中的目录与 manifest 清单。你应看到 `.agents/skills/oneirloom/SKILL.md`、`.agents/skills/oneirloom-craft-construction/SKILL.md` 等 22 个入口；各自引用的 references、templates 和其他包内文件仍在原相对位置。
4. 保留下载的 ZIP、校验文件和 manifest，作为这次安装的记录。升级时只处理这次清单明确拥有的 Oneirloom 目录，不用通配符删除全部 `oneirloom*`，也不删除整个 `.agents/skills/`。

## 在新聊天确认实际路径

在 Codex 中打开目标项目，再创建**新聊天**。可以发送：

```text
请从当前项目的 .agents/skills/oneirloom/SKILL.md 读取 Oneirloom，并告诉我实际读取的绝对路径。再读取它引用的共享交互约定，报告该文件的实际路径。按我接下来给出的商品资料开始任务。
```

确认返回路径属于你刚安装的项目。然后调用 `$oneirloom`，或点名一个已安装的方法。若助手读取的是全局目录或插件缓存，先定位当前项目副本；同名全局技能可能遮住项目副本，旧聊天也可能保留较早的指令。文件已复制和这次聊天实际读取了项目副本，是两个需要分别确认的步骤。

ZIP 上传到普通聊天不会完成项目安装。这里交付的是提示词与创作方法；图像生成使用你实际可用的工具或服务。

## 历史 18 技能包

`0.2.0-preview.1` 是保留的旧固定版本，包含 18 项技能；它与本次 22 项版本各自有独立清单和校验值。需要查看旧版时，使用[历史发布页](https://github.com/PigeonAI-Yang/oneirloom/releases/tag/v0.2.0-preview.1)、[旧 ZIP](https://github.com/PigeonAI-Yang/oneirloom/releases/download/v0.2.0-preview.1/oneirloom-0.2.0-preview.1.zip)及[旧校验文件](https://github.com/PigeonAI-Yang/oneirloom/releases/download/v0.2.0-preview.1/SHA256SUMS.txt)。旧 ZIP 的 SHA-256 仍是 `38abe37cfa430f4876fb573f94e7d17d3344681513d9c3c77a29781ce24bbb4b`；旧 manifest 的 SHA-256 是 `d9f9384c8111da20cb4a52ca401826b4a8ac3f91e0e5834b06d664ce03d1ebd4`。

这篇当前教程保持免费。此前 `draft-1` 的原文与版本作为[历史安装教程](https://www.pigeonyang.top/learn/oneirloom.learning.install-fixed-package~40draft-1/)保留；它记录的是旧版发布阶段，当前安装请按本篇的 22 项固定包操作。
