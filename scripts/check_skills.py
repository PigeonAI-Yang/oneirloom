#!/usr/bin/env python3
"""Small structural check for the router and independently usable child skills."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {
    "oneirloom",
    "oneirloom-visual-analysis",
    "oneirloom-camera-composition",
    "oneirloom-color-light",
    "oneirloom-style-photography",
    "oneirloom-style-illustration",
    "oneirloom-style-design",
    "oneirloom-model-krea-2",
    "oneirloom-model-qwen-image-2-1",
    "oneirloom-result-diagnosis",
}


def check() -> None:
    found = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    assert found == EXPECTED, f"skill set differs: missing={EXPECTED-found}, extra={found-EXPECTED}"
    for name in sorted(EXPECTED):
        path = SKILLS / name / "SKILL.md"
        body = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", body, re.S)
        assert match, f"missing frontmatter: {path}"
        metadata = dict(re.findall(r"^(name|description):\s*(.+)$", match.group(1), re.M))
        assert metadata.get("name") == name, f"frontmatter name mismatch: {path}"
        assert metadata.get("description"), f"description missing: {path}"
        assert len(name) < 64 and re.fullmatch(r"[a-z0-9-]+", name), name
        assert len(body) < 20000, f"keep SKILL.md concise: {path}"
        for target in re.findall(r"\]\(([^)]+)\)", body):
            if "://" not in target and not target.startswith("#"):
                assert (path.parent / target).is_file(), f"broken skill link: {path}: {target}"
    router = (SKILLS / "oneirloom" / "SKILL.md").read_text(encoding="utf-8")
    for name in EXPECTED - {"oneirloom"}:
        assert f"`{name}`" in router, f"router does not mention {name}"
    cases = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
    ids = [case["id"] for case in cases]
    assert len(ids) == len(set(ids)) and len(ids) >= 8
    for case in cases:
        assert case["input"] and case["expected"] and case["failure"]
    for example in (ROOT / "examples").glob("*.md"):
        content = example.read_text(encoding="utf-8")
        assert "```text\n" in content, f"missing copyable prompt: {example}"
        prompt = content.split("```text\n", 1)[1].split("\n```", 1)[0]
        assert not re.search(r"(^|[，。；\s])(不要|避免|排除|negative prompt|not dull)\b", prompt, re.I), example
    print(f"OK: {len(EXPECTED)} skills, {len(cases)} behavior cases, 2 example prompts")


if __name__ == "__main__":
    check()
