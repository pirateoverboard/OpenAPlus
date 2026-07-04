# OpenAPlus agent instructions

This repository builds OpenAPlus, an open-source learning platform for CompTIA
certification study materials. Agents must follow the repository documentation
before creating, reviewing, or modifying educational content.

## Required reading

Before changing content, pipeline behavior, generated output, or review records,
read the docs that apply to the task. At minimum, content-authoring or review
work must consult:

- [docs/CONTENT_CREATION_RULES.md](docs/CONTENT_CREATION_RULES.md)
- [docs/CARD_SCHEMA.md](docs/CARD_SCHEMA.md)
- [docs/HINTS.md](docs/HINTS.md)
- [docs/TAGGING.md](docs/TAGGING.md)
- [docs/SOURCE_AND_CITATION_RULES.md](docs/SOURCE_AND_CITATION_RULES.md)
- [docs/OBJECTIVE_COMPLETION_CHECKLIST.md](docs/OBJECTIVE_COMPLETION_CHECKLIST.md)
- [docs/ANKI_IMPORT.md](docs/ANKI_IMPORT.md)
- [docs/IMAGE_WORKFLOW.md](docs/IMAGE_WORKFLOW.md)
- [docs/OpenAPlus_Review_Prompt_Pack.md](docs/OpenAPlus_Review_Prompt_Pack.md)
- [docs/INTERVIEW_TROUBLESHOOTING.md](docs/INTERVIEW_TROUBLESHOOTING.md)

## Documentation index

All files currently under `docs/`:

- [docs/ANKI_IMPORT.md](docs/ANKI_IMPORT.md) — Anki TSV import settings,
  media installation, smoke-test procedure, and note-type expectations.
- [docs/CARD_AUTHORING_GUIDE.md](docs/CARD_AUTHORING_GUIDE.md) — When to use
  Basic, Cloze, and Image cards; atomicity and scenario-card guidance.
- [docs/CARD_QUALITY_EXAMPLES.md](docs/CARD_QUALITY_EXAMPLES.md) — Bad,
  okay, and great card examples for contributor self-review.
- [docs/CARD_SCHEMA.md](docs/CARD_SCHEMA.md) — Markdown/YAML card schema,
  required metadata, rendered fields, difficulty rubric, and section rules.
- [docs/CLOZE_GUIDE.md](docs/CLOZE_GUIDE.md) — Cloze-card use cases and quality
  rules.
- [docs/CONTENT_CREATION_RULES.md](docs/CONTENT_CREATION_RULES.md) — Core
  content philosophy, source-backed authoring rules, and objective workflow.
- [docs/IMAGE_CARD_GUIDE.md](docs/IMAGE_CARD_GUIDE.md) — Occlusion-style image
  card behavior and original-diagram requirements.
- [docs/IMAGE_WORKFLOW.md](docs/IMAGE_WORKFLOW.md) — Future workflow for
  safely adding real photos, especially Wikimedia Commons images, with license
  review and attribution tracking.
- [docs/HINTS.md](docs/HINTS.md) — Optional `## Hint` section policy,
  pre-reveal usage, and bad/okay/great hint examples.
- [docs/INTERVIEW_TROUBLESHOOTING.md](docs/INTERVIEW_TROUBLESHOOTING.md) —
  Guidance for objective-local troubleshooting interview-practice files and
  the boundary between broad spoken answers and regular Anki cards.
- [docs/INSTRUCTOR_NOTES_GUIDE.md](docs/INSTRUCTOR_NOTES_GUIDE.md) —
  Instructor Notes policy and acceptable note sections.
- [docs/LICENSE](docs/LICENSE) — Documentation/content license file.
- [docs/OBJECTIVE_COMPLETION_CHECKLIST.md](docs/OBJECTIVE_COMPLETION_CHECKLIST.md)
  — Required objective completion, coverage mapping, review, and acceptance
  workflow.
- [docs/OpenAPlus_Review_Prompt_Pack.md](docs/OpenAPlus_Review_Prompt_Pack.md)
  — Review prompt templates and maintainer review workflow guidance.
- [docs/README.md](docs/README.md) — Documentation directory overview.
- [docs/SOURCE_AND_CITATION_RULES.md](docs/SOURCE_AND_CITATION_RULES.md) —
  Source priority, paraphrasing, ambiguity handling, and citation rules.
- [docs/TAGGING.md](docs/TAGGING.md) — Derived tag policy, custom tag rules,
  HighYield rubric, and domain/source-validation tags.

## Source handling

Private reference sources may be used only as private references. Do not commit
PDFs, screenshots, OCR exports, copied tables, copied diagrams, or long copied
passages. OpenAPlus content must use original wording, original explanations,
original examples, and original diagrams. Cite sources by concise page or
objective reference.

Use CompTIA exam objectives as the primary scope authority. Use approved
secondary sources, such as Professor Messer notes, only to validate concept
presence and page references unless the user explicitly authorizes another
approved source.

## Content boundaries

- Work on one objective at a time unless explicitly instructed otherwise.
- Do not modify accepted objectives unless the task explicitly asks for it.
- Do not start the next objective preemptively.
- Do not add APKG generation, PDF generation, website rendering, native image
  occlusion, full practice exams, or large content expansions unless explicitly
  requested.
- Do not manually add derived tags to card front matter. Author tags are custom
  topic tags only.

## Verification

For content or pipeline changes, run the relevant checks before handoff:

```bash
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build.py
.venv/bin/python -m pytest
.venv/bin/ruff check .
.venv/bin/ruff format --check .
```

If website files or website-facing docs are changed, also run:

```bash
npm --prefix website run typecheck
npm --prefix website run build
```

Generated TSV output is part of the repository contract. Regenerate it after
card or pipeline changes and verify that unrelated accepted objectives were not
modified.
