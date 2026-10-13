---
article_id: oneirloom.learning.install-fixed-package
version: draft-1
date: 2026-10-11
locale: zh-CN
title_zh: "安装已发布的固定包"
title_en: "Install the published fixed package"
sources:
  - "[现有安装说明](../INSTALL.md)"
  - "[冻结包发布记录](../releases/0.2.0-preview.1-publication.md)"
evidence: "Authored guidance; no image rendered; no new installed behavior claim."
---

# 安装已发布的固定包

本路径安装发布的 `0.2.0-preview.1`。当前开发源 `0.3.0-preview` 有 22 个技能，但没有与该源版本对应的发布包；固定 ZIP 是另一个版本，包含 18 个技能。要安装已发布版本，请始终按 ZIP 内的 `SOURCE-MANIFEST.json` 和现有[安装说明](../INSTALL.md)核对。

## 下载并核对发布文件

从已发布的固定地址下载 [oneirloom-0.2.0-preview.1.zip](https://github.com/PigeonAI-Yang/oneirloom/releases/download/v0.2.0-preview.1/oneirloom-0.2.0-preview.1.zip) 和 [SHA256SUMS.txt](https://github.com/PigeonAI-Yang/oneirloom/releases/download/v0.2.0-preview.1/SHA256SUMS.txt)。发布记录写明 ZIP 为 104,730,348 字节，SHA-256 为 `38abe37cfa430f4876fb573f94e7d17d3344681513d9c3c77a29781ce24bbb4b`；包内 `SOURCE-MANIFEST.json` 的记录哈希为 `d9f9384c8111da20cb4a52ca401826b4a8ac3f91e0e5834b06d664ce03d1ebd4`。

在下载目录运行现有安装说明中的命令，再将结果与校验文件里**同名 ZIP**的条目比较：

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath './oneirloom-0.2.0-preview.1.zip'
```

## 安装到项目

1. 将 ZIP 解压到一个新目录，在含有 `skills/` 和 `SOURCE-MANIFEST.json` 的包根目录操作。核对 manifest 中的包版本为 `0.2.0-preview.1`，并确认它列出 18 个技能目录。
2. 优先在空白 Codex 项目安装。若目标项目已有 `.agents/skills/` 或 Oneirloom 本地修改，先保留原目录并备份；不要覆盖来源不明的目录，也不要用通配符清理其他技能。需要升级时，按[安装说明中的备份与恢复步骤](../INSTALL.md)处理。
3. 把 manifest 列出的 18 个完整同级目录复制到项目的 `.agents/skills/`，保留每个目录名和内部文件。不要再套一层 `oneirloom/`。
4. 在该项目打开新聊天。确认宿主从这个项目路径发现技能，再调用 `$oneirloom` 或点名一个已安装的方法。留意全局同名技能可能遮住项目副本；如有疑问，核对助手实际读取的文件路径。旧聊天可能仍使用较早的指令。

这条路径只使用现有项目级安装步骤。ZIP 上传到普通聊天不会完成安装；开发源中新增的文件也不会因此进入冻结的 18 技能 ZIP。
