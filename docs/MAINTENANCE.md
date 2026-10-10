# Maintain project metadata

`scripts/sync_project_metadata.py` keeps repository metadata in sync with the source skills and frozen package. It reads the version from `.codex-plugin/plugin.json`, discovers immediate `skills/*/SKILL.md` entries, reads the frozen package inventory from `SOURCE-MANIFEST.json`, and takes bilingual names and short descriptions from `docs/project-copy.json`.

The generated website data lives at `docs/project-status.json`. It contains the current source version and skill IDs, frozen package version and download links, bilingual copy, and GitHub description. A site copy uses the same JSON bytes at `content/oneirloom-project.json`.

The tool also updates named generated regions in both READMEs, the installation guide, the architecture and compatibility status paragraphs, and the current-source row in `PROJECT-FILES.md`. Those regions take source and frozen-package versions and counts from the metadata inputs. Dated release records and the historical compatibility table remain maintained as records.

Run the default check before committing metadata changes:

```powershell
python scripts/sync_project_metadata.py --check --json
```

The check writes nothing and uses no network. Exit code `0` means generated files match. Exit code `1` reports drift. Exit code `2` reports invalid input or an operational error.

After changing the source version or adding or removing a skill, update generated repository files with:

```powershell
python scripts/sync_project_metadata.py --write
```

Add one entry to `docs/project-copy.json` for every current skill ID. Each entry has `zh`, `en`, `zhDescription`, and `enDescription`. The file contains labels only. The tool derives counts and versions from source files and rejects missing or extra IDs before it writes anything.

To copy the generated artifact into a site checkout, provide its existing root:

```powershell
python scripts/sync_project_metadata.py --write --site-root C:\path\to\oneirloom-site --json
```

The site root must contain a `package.json` whose name is `oneirloom`, `scripts/skill-pages.mjs`, and an existing `content/` directory. The command changes only `content/oneirloom-project.json` in that checkout. It does not create directories or edit site source files.

`--github-check` reads the repository description and compares it with the artifact. `--github-sync` updates only that description, then reads it back. The sync flag requires `--write`. Neither GitHub option runs by default.

For example, a maintainer can update repository files, copy the artifact, and sync the repository description in one explicit command:

```powershell
python scripts/sync_project_metadata.py --write --site-root C:\path\to\oneirloom-site --github-sync --json
```

The command does not package or publish a release, install skills, commit changes, or deploy the website. Use the existing authorized project workflows for those operations.
