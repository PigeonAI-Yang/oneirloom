# Oneirloom plugin submission status

Oneirloom 0.1.1 is a skills-only package with 15 skills and an MIT license. It includes no MCP server, connected account, or lifecycle hooks. The Qwen-Image-2.1 reference materials carry a separate license and attribution notice.

The corrected local 0.1.1 candidate was enabled on Codex CLI 0.153.0. Its 117 ZIP entries matched the extracted package and installed cache by hash and size; eight Git LFS objects were hydrated, no pointers remained, and all 25 raster images decoded. `skills/list` found all 15 skills with zero candidate-specific errors. This verifies the package through a local marketplace candidate, not installation from the public GitHub marketplace or OpenAI directory approval. The optional prompt-card renderer previously passed a separate local synthetic-image check.

The package has **not** been submitted to or listed in the OpenAI plugin directory. The homepage and privacy-policy URLs still need live verification. See [SUBMISSION.md](SUBMISSION.md) for the complete publisher checklist covering organization and project ownership, developer verification, rights review, URL checks, policy attestations, upload, review, and publication.
