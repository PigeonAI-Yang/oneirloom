param(
    [string]$ProjectPath = 'J:\pigeonyang\skills\oneirloom'
)

$ErrorActionPreference = 'Stop'
if (-not (Test-Path -LiteralPath (Join-Path $ProjectPath '.git'))) {
    throw "请先把项目归档解压到 $ProjectPath；目录必须包含 .git。"
}
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw '找不到 git。'
}
& git -C $ProjectPath var GIT_AUTHOR_IDENT | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw '本机 Git 作者身份未配置。请先在本机配置 user.name 和 user.email。'
}
& git -C $ProjectPath var GIT_COMMITTER_IDENT | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw '本机 Git 提交者身份未配置。'
}
& git -C $ProjectPath status --short
if ($LASTEXITCODE -ne 0) { throw 'Git 状态检查失败。' }
& git -C $ProjectPath add --all
if ($LASTEXITCODE -ne 0) { throw 'Git 暂存失败。' }
& git -C $ProjectPath diff --cached --quiet
if ($LASTEXITCODE -eq 1) {
    & git -C $ProjectPath commit -m 'Initial open-source skill architecture'
    if ($LASTEXITCODE -ne 0) { throw 'Git 提交失败。' }
} elseif ($LASTEXITCODE -ne 0) {
    throw 'Git 差异检查失败。'
}
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw '本地提交已完成。找不到 GitHub CLI gh；安装并登录后再创建公开仓库。'
}
& gh auth status
if ($LASTEXITCODE -ne 0) { throw '本地提交已完成。请先执行 gh auth login。' }
$remotes = & git -C $ProjectPath remote
if ($LASTEXITCODE -ne 0) { throw '无法读取 Git 远端。' }
if ($remotes -contains 'origin') { throw '已存在 origin 远端；请先确认目标仓库，脚本未覆盖。' }
& gh repo create oneirloom --public --source $ProjectPath --remote origin --push --description 'Oneirloom: modular image prompt skills for Krea 2 and Qwen-Image-2.1'
if ($LASTEXITCODE -ne 0) { throw '公开仓库创建或推送失败；本地提交仍保留。' }
& git -C $ProjectPath remote get-url origin
