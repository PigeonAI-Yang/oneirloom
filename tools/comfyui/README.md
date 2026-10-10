# Oneirloom local ComfyUI tool

`generate.ps1` submits one text-to-image job to the Krea 2 API workflow, waits for that exact prompt, and retrieves its PNG from ComfyUI's local `/view` endpoint. It only accepts loopback URLs. It refuses to add a job while the ComfyUI queue is busy, and it never retries a submission whose result is unknown.

Run from the repository root in PowerShell 7:

```powershell
pwsh -NoProfile -File .\tools\comfyui\generate.ps1 `
  -Prompt '一位成年女性坐在窗边，柔和的伦勃朗光，人物占画面高度45%' `
  -Width 888 -Height 1184 -Steps 8 -Seed 42
```

Omit `-Seed` for a random seed. The returned JSON contains the saved image path, prompt ID, seed, dimensions, and receipt path. PNG files and small request receipts go to `output/comfyui/` by default. Pass `-OutputDirectory`, `-OutputPrefix`, `-Cfg`, `-SamplerName`, `-Scheduler`, `-UnetName`, `-ClipName`, or `-VaeName` to override those defaults.

If a caller loses its connection after submitting, retrieve an already submitted prompt without creating a second job:

```powershell
pwsh -NoProfile -File .\tools\comfyui\generate.ps1 -ResumePromptId 'PROMPT-ID'
```

The bundled API workflow uses the locally installed Krea 2 model filenames. `-WorkflowPath` can select another API-format workflow if it keeps the template node IDs used by the script: 29 SaveImage, 51 CLIPTextEncode, 52 UNETLoader, 53 CLIPLoader, 54 KSampler, 57 EmptyLatentImage, and 58 VAELoader.
