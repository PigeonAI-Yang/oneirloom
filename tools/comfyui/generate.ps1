#requires -Version 7.0
[CmdletBinding()]
param(
    [string]$Prompt = '',

    [string]$ResumePromptId = '',

    [string]$ApiUrl = 'http://127.0.0.1:8188',

    [string]$WorkflowPath = (Join-Path $PSScriptRoot 'krea2-api-workflow.json'),

    [ValidateRange(64, 8192)]
    [int]$Width = 888,

    [ValidateRange(64, 8192)]
    [int]$Height = 1184,

    [long]$Seed = -1,

    [ValidateRange(1, 150)]
    [int]$Steps = 8,

    [ValidateRange(0, 30)]
    [double]$Cfg = 1.0,

    [string]$SamplerName = 'er_sde',

    [string]$Scheduler = 'simple',

    [string]$UnetName = 'moodyKrea2Mix_v40BF16.safetensors',

    [string]$ClipName = 'QWEN\QWEN_VL\Qwen3-VL-4B-Instruct-Heretic.safetensors',

    [string]$VaeName = 'krea2RealVae_v10.safetensors',

    [string]$OutputPrefix = '',

    [string]$OutputDirectory = '',

    [ValidateRange(1, 3600)]
    [int]$TimeoutSeconds = 900,

    [ValidateRange(1, 60)]
    [int]$PollSeconds = 5
)

$ErrorActionPreference = 'Stop'

$api = [uri]$ApiUrl
if (-not $api.IsLoopback -or $api.Scheme -ne 'http') {
    throw 'ApiUrl must be an HTTP loopback address such as http://127.0.0.1:8188.'
}

if (($Width % 8) -ne 0 -or ($Height % 8) -ne 0) {
    throw 'Width and Height must both be divisible by 8.'
}

if ([string]::IsNullOrWhiteSpace($ResumePromptId) -and [string]::IsNullOrWhiteSpace($Prompt)) {
    throw 'Pass -Prompt to submit a new image or -ResumePromptId to retrieve an existing result.'
}

if ([string]::IsNullOrWhiteSpace($ResumePromptId) -and -not (Test-Path -LiteralPath $WorkflowPath -PathType Leaf)) {
    throw "Workflow file not found: $WorkflowPath"
}

if ([string]::IsNullOrWhiteSpace($OutputDirectory)) {
    $OutputDirectory = Join-Path (Split-Path (Split-Path $PSScriptRoot -Parent) -Parent) 'output\comfyui'
}

$OutputDirectory = [System.IO.Path]::GetFullPath($OutputDirectory)
$null = New-Item -ItemType Directory -Path $OutputDirectory -Force

if ([string]::IsNullOrWhiteSpace($OutputPrefix)) {
    $OutputPrefix = 'oneirloom_' + (Get-Date -Format 'yyyyMMdd_HHmmss')
}

if ($OutputPrefix -notmatch '^[A-Za-z0-9_-]+$') {
    throw 'OutputPrefix may contain only ASCII letters, numbers, underscores, and hyphens.'
}

if ([string]::IsNullOrWhiteSpace($ResumePromptId)) {
    $workflow = Get-Content -LiteralPath $WorkflowPath -Raw -Encoding UTF8 | ConvertFrom-Json -AsHashtable
    foreach ($nodeId in @('29', '51', '52', '53', '54', '57', '58')) {
        if (-not $workflow.ContainsKey($nodeId)) {
            throw "Workflow is missing required node $nodeId."
        }
    }

    $workflow['29']['inputs']['filename_prefix'] = $OutputPrefix
    $workflow['51']['inputs']['text'] = $Prompt
    $workflow['52']['inputs']['unet_name'] = $UnetName
    $workflow['53']['inputs']['clip_name'] = $ClipName
    $workflow['54']['inputs']['seed'] = if ($Seed -lt 0) { Get-Random -Minimum 1 -Maximum ([int]::MaxValue) } else { $Seed }
    $workflow['54']['inputs']['steps'] = $Steps
    $workflow['54']['inputs']['cfg'] = $Cfg
    $workflow['54']['inputs']['sampler_name'] = $SamplerName
    $workflow['54']['inputs']['scheduler'] = $Scheduler
    $workflow['57']['inputs']['width'] = $Width
    $workflow['57']['inputs']['height'] = $Height
    $workflow['58']['inputs']['vae_name'] = $VaeName

    $queue = Invoke-RestMethod -Uri "$($api.AbsoluteUri.TrimEnd('/'))/queue" -TimeoutSec 10
    if (@($queue.queue_running).Count -gt 0 -or @($queue.queue_pending).Count -gt 0) {
        throw 'ComfyUI already has a running or queued job. The tool left that queue unchanged.'
    }

    $clientId = [guid]::NewGuid().ToString()
    $stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
    $requestPath = Join-Path $OutputDirectory "$($OutputPrefix)_$($stamp)_request.json"
    $receiptPath = Join-Path $OutputDirectory "$($OutputPrefix)_$($stamp)_receipt.json"
    $request = [ordered]@{
        prompt = $workflow
        client_id = $clientId
    }
    $receipt = [ordered]@{
        status = 'prepared'
        client_id = $clientId
        seed = $workflow['54']['inputs']['seed']
        request_path = $requestPath
        receipt_path = $receiptPath
    }
    $request | ConvertTo-Json -Depth 100 | Set-Content -LiteralPath $requestPath -Encoding UTF8
    $receipt | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $receiptPath -Encoding UTF8

    try {
        $submitted = Invoke-RestMethod -Uri "$($api.AbsoluteUri.TrimEnd('/'))/prompt" -Method Post -ContentType 'application/json' -Body ($request | ConvertTo-Json -Depth 100 -Compress) -TimeoutSec 20
    }
    catch {
        $receipt.status = 'post_outcome_unknown'
        $receipt.error = $_.Exception.Message
        $receipt | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $receiptPath -Encoding UTF8
        throw "Submission outcome is unknown. Do not submit again until client_id $clientId has been reconciled. $($_.Exception.Message)"
    }

    $nodeErrors = $submitted.node_errors
    if ($null -ne $nodeErrors -and @($nodeErrors.PSObject.Properties).Count -gt 0) {
        $receipt.status = 'rejected'
        $receipt.response_node_errors = $nodeErrors
        $receipt | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $receiptPath -Encoding UTF8
        throw "ComfyUI rejected the workflow. Receipt: $receiptPath"
    }

    $promptId = [string]$submitted.prompt_id
    if ([string]::IsNullOrWhiteSpace($promptId)) {
        $receipt.status = 'missing_prompt_id'
        $receipt | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $receiptPath -Encoding UTF8
        throw "ComfyUI accepted no prompt ID. Inspect receipt: $receiptPath"
    }

    $receipt.status = 'submitted'
    $receipt.prompt_id = $promptId
    $receipt | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $receiptPath -Encoding UTF8
}
else {
    $parsedPromptId = [guid]::Empty
    if (-not [guid]::TryParse($ResumePromptId, [ref]$parsedPromptId)) {
        throw 'ResumePromptId must be the GUID returned by a previous ComfyUI submission.'
    }
    $promptId = $parsedPromptId.ToString()
    $stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
    $receiptPath = Join-Path $OutputDirectory "$($OutputPrefix)_$($stamp)_receipt.json"
    $receipt = [ordered]@{
        status = 'tracking'
        prompt_id = $promptId
        receipt_path = $receiptPath
    }
    $receipt | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $receiptPath -Encoding UTF8
}

$deadline = (Get-Date).AddSeconds($TimeoutSeconds)
$historyUri = "$($api.AbsoluteUri.TrimEnd('/'))/history/$promptId"

while ((Get-Date) -lt $deadline) {
    $history = Invoke-RestMethod -Uri $historyUri -TimeoutSec 20
    $entryProperty = $history.PSObject.Properties[$promptId]
    if ($null -ne $entryProperty) {
        $entry = $entryProperty.Value
        $status = [string]$entry.status.status_str
        if ($status -eq 'error') {
            $receipt.status = 'error'
            $receipt.history_status = $entry.status
            $receipt | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $receiptPath -Encoding UTF8
            throw "ComfyUI generation failed. Receipt: $receiptPath"
        }

        if ($status -eq 'success' -or $entry.status.completed) {
            $image = $null
            foreach ($output in $entry.outputs.PSObject.Properties) {
                if (@($output.Value.images).Count -gt 0) {
                    $image = $output.Value.images[0]
                    break
                }
            }
            if ($null -eq $image) {
                $receipt.status = 'success_without_image'
                $receipt | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $receiptPath -Encoding UTF8
                throw "Generation completed without an image. Receipt: $receiptPath"
            }

            $imageName = [System.IO.Path]::GetFileName([string]$image.filename)
            if ($imageName -ne [string]$image.filename -or $imageName -notmatch '\.png$') {
                throw 'ComfyUI returned an unexpected image filename.'
            }
            $query = 'filename={0}&subfolder={1}&type=output' -f [uri]::EscapeDataString($imageName), [uri]::EscapeDataString([string]$image.subfolder)
            $imagePath = Join-Path $OutputDirectory $imageName
            Invoke-WebRequest -Uri "$($api.AbsoluteUri.TrimEnd('/'))/view?$query" -OutFile $imagePath -TimeoutSec 30
            $signature = [System.IO.File]::ReadAllBytes($imagePath)
            if ($signature.Length -lt 24 -or $signature[0] -ne 137 -or $signature[1] -ne 80 -or $signature[2] -ne 78 -or $signature[3] -ne 71) {
                throw "ComfyUI result is not a valid PNG: $imagePath"
            }

            $width = [System.Net.IPAddress]::NetworkToHostOrder([BitConverter]::ToInt32($signature, 16))
            $height = [System.Net.IPAddress]::NetworkToHostOrder([BitConverter]::ToInt32($signature, 20))
            $receipt.status = 'success'
            $receipt.image_path = $imagePath
            $receipt.image_bytes = $signature.Length
            $receipt.width = $width
            $receipt.height = $height
            $receipt.completed_at = (Get-Date).ToString('o')
            $receipt | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $receiptPath -Encoding UTF8
            [pscustomobject]$receipt | ConvertTo-Json -Depth 20
            return
        }
    }
    Start-Sleep -Seconds $PollSeconds
}

$receipt.status = 'still_running'
$receipt | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $receiptPath -Encoding UTF8
throw "Generation is still running as prompt_id $promptId. Check that job before requesting another generation."
