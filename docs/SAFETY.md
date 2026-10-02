# Safety, privacy, and third-party material

## Data flow

This package contains skill instructions and one optional local renderer. It bundles no MCP server, account connection, background service, telemetry uploader, or automatic upload process. The optional prompt-card renderer reads the image and prompt selected by the user and writes files to the chosen local output directory. Its Python imports are Pillow and Playwright; the browser and file permissions belong to the host environment.

Some workflows may use image, browser, or generation tools supplied by the host. The host and selected service determine how supplied content is processed. Review the host's privacy terms before sharing personal, confidential, or unpublished images. Share only material you have permission to use, and approve any external upload yourself.

The plugin's public metadata contains website, support, and privacy-policy URLs. Keep private credentials and user information out of public listing fields, archives, and examples. Live reachability and content for the website and privacy URLs remain unverified; verify them before submission.

## Third-party rights

The Qwen official reference archive includes a separate research license and its required attribution notice. See [Third-party notices](../THIRD_PARTY_NOTICES.md) and the `LICENSE` and `Notice` files under `skills/oneirloom-model-qwen-image-2-1/references/official/`. The license grants non-commercial research or evaluation use; commercial use requires a separate permission from the rights holder.

The package's root MIT license does not grant rights in third-party images, examples, or archived reference materials. Source provenance or prior acceptance is not an independent redistribution grant. The publisher must review and attest to the relevant rights before external submission.