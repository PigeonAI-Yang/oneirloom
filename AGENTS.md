# Oneirloom project rules

Use [Project file index](PROJECT-FILES.md) to locate project assets, skills, deliveries, and verification records. Update that index when adding or organizing project files; keep detailed file lists out of this rules file.

## Private brand VI assets

Oneirloom brand VI assets are private and must remain local. Do not commit, push, publish, or deploy mascot source art, identity sheets, logo and icon variants, standalone brand watermarks, branded sticker assets, or delivery archives containing them. Only individual brand assets directly required by the website may be excepted; keep those exceptions explicit and minimal in .gitignore. Completed image cases and showcase imagery are a separate category and remain publishable under the current task authorization, including finished images containing branding. Do not blanket-ignore images, output, or work directories. Ignore rules do not remove tracked files or historical objects: prepare publication commits without private VI assets, preserve local files and original commits, and never push a local private-history backup branch.

## Project metadata maintenance

- After changing `.codex-plugin/plugin.json` version or the set of `skills/*/SKILL.md` entries, run `python scripts/sync_project_metadata.py --write` to update generated project metadata.
- Run `python scripts/sync_project_metadata.py --check --json` before committing metadata changes.
- The default check makes no writes and uses no network. `--site-root` writes only `content/oneirloom-project.json` under an existing validated site root.
- Use `--github-sync` only when the GitHub repository description should change. That option requires `--write` and reads back the updated description.
