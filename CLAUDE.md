# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository distills books into executable Claude Code Skills using the **RIA-TV++ pipeline**. Each book is processed into a set of structured `SKILL.md` files that Claude Code can invoke via `/skill-name`.

Currently contains 4 books:
- `30岁人生开挂7步法` — 16 skills
- `小狗钱钱` (Kira & The Secret of a Money) — 20 skills
- `置身事内：中国政府与经济发展` — 20 skills
- `金钱的属性：一个富豪的财富私房课` — 26 skills

## Directory Structure (per book)

```
📂 <book-dir>/
├── 📂 v01-<skill-name>/   # Individual skill directory
│   └── SKILL.md           # RIA++ format skill definition
├── 📂 v02-<skill-name>/
│   └── SKILL.md
├── 📂 candidates/          # Raw concept candidates before SKILL.md distillation
├── 📂 rejected/            # Proposals that failed validation
├── INDEX.md                # Skill relationship network, dependencies, usage paths
├── BOOK_OVERVIEW.md        # Book summary and distillation notes
├── test-prompts.json       # Test prompts matching each skill's trigger scenarios
├── verified.md             # Triple validation records (V1: evidence, V2: prediction, V3: exclusivity)
├── *.epub / *.txt          # Original book source files
└── extract_book.py         # Optional extraction script
```

## SKILL.md Format (RIA++ Template)

Each skill file uses YAML frontmatter + RIA++ sections:

```yaml
---
name: Skill Name
description: |
  When should this skill activate? What problems does it solve?
source_book: 《Book Title》Author
source_chapter: Chapter reference
tags: [tag1, tag2]
related_skills: [vXX-other-skill]
---
```

Sections (R-I-A-A-E-B):
- **R (Reading)** — Core quote from the book
- **I (Interpretation)** — Underlying principle / methodology
- **A1 (Past Application)** — Book case studies, concrete examples
- **A2 (Future Triggers)** — When to use this skill in real life
- **E (Execution Steps)** — Runnable action plan
- **B (Boundary)** — Limitations and edge cases

## INDEX.md Structure

INDEX.md is the skill relationship network. It contains:
- Skill dependency graph (prerequisites, usage order)
- Skill classification (type, frequency, capability category)
- Recommended learning/usage paths (multiple paths for different goals)
- Comparison tables between related skills
- Skill combinations (which skills work together and why)

## test-prompts.json Formats

Two variants exist across books:

**Variant A (30岁人生开挂7步法)** — object keyed by skill ID, with `expected_framework` and `expected_approach`:
```json
{
  "v01-skill-name": [
    {
      "prompt": "user trigger text",
      "expected_framework": "...",
      "expected_approach": "..."
    }
  ]
}
```

**Variant B (小狗钱钱, 置身事内)** — array with explicit `skill` field and `category`:
```json
[
  {
    "skill": "v01-skill-name",
    "prompts": [
      {"prompt": "...", "expected_skill": "v01", "category": "should_invoke"},
      {"prompt": "...", "expected_skill": null, "category": "should_not_invoke"}
    ]
  }
]
```

## Key Commands

No build system, package manager, or test framework — this is a content repository. Common operations:

- **Generate skills**: Run book-specific extraction scripts (`python extract_book.py` or `python write_skills.py`)
- **Validate skills**: Review `verified.md` triple validation records
- **Add a new book**: Create `<book-dir>/` with the standard directory structure (v01-*/, candidates/, rejected/, INDEX.md, BOOK_OVERVIEW.md, test-prompts.json, verified.md)
- **Test skill triggering**: Use prompts from `test-prompts.json` in Claude Code to verify skill invocation

## Architecture Notes

- **RIA-TV++ pipeline**: Referenced at `https://github.com/R2h/cangjie-skill` — the external pipeline used for distillation
- **Triple validation (V1-V3)**: Every skill candidate passes V1 (cross-domain evidence), V2 (predictive power), V3 (exclusivity) before becoming a SKILL.md
- **Skills directory naming**: `vXX-name` format (zero-padded, two digits), e.g., `v01-摆脱自我意识三步法`
- **All content is Chinese (Simplified)**: UI strings, documentation, and SKILL.md content are all written in Chinese
