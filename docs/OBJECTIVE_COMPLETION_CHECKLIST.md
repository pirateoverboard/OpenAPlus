# Objective completion checklist

Complete this checklist for each objective. A checked item means the artifact
was reviewed, not merely created.

## Research and extraction

- [ ] The matching exam version and objective scope are confirmed.
- [ ] Sources were reviewed according to their defined scope and authoring roles.
- [ ] Concepts were extracted without copying source language.
- [ ] Ambiguities were recorded in `changelog.md` and resolved.

## Coverage map

Maintain this table in the objective's `checklist.md`. Add one row for every
extracted concept. Coverage means every concept has a reviewed disposition; it
does not mean every concept must become a card.

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| SO-DIMM | Professor Messer p.1 | Laptop Memory | 1.1-B001, 1.1-C001 | Basic, Cloze | N/A | Yes |
| `[concept without a card]` | `[source]` | `[section]` | None | None | `[reviewed reason]` | Yes/No |

Use `None` only with a specific no-card reason, such as study-guide coverage
being sufficient or the detail being out of scope. Do not create filler cards
to eliminate `None` entries.

## Authoring

- [ ] `study-guide.md` is written, sourced, and internally consistent.
- [ ] Basic cards cover justified application, scenario, or reasoning needs.
- [ ] Cloze cards cover justified short-recall needs without excessive deletions.
- [ ] Image cards were considered and created only when visual recognition adds
      learning value.
- [ ] `checklist.md` reflects the objective's actual concepts and coverage.
- [ ] Instructor Notes add concise value rather than repeat answers.
- [ ] Any omitted Instructor Notes have a reviewed justification in this
      checklist or `changelog.md`.
- [ ] Every HighYield card has reviewer agreement or a documented justification.
- [ ] Custom tags and stable IDs follow repository rules.
- [ ] `changelog.md` records the objective's authoring and review changes.

## Review and build

- [ ] Every factual claim and card has a reviewable source.
- [ ] Cards were peer reviewed for accuracy, atomicity, wording, and ambiguity.
- [ ] Original diagrams were reviewed for clarity, licensing, and unique names.
- [ ] `python scripts/validate.py` passes without unexplained warnings.
- [ ] `python scripts/build.py` passes and removes no expected output.
- [ ] Generated TSV changes are committed with their Markdown sources.
- [ ] `pytest`, Ruff, and Docusaurus checks pass.
- [ ] Every smoke test required by [ANKI_IMPORT.md](ANKI_IMPORT.md) was performed
      and passed, or the objective is explicitly outside its required cases.

## Peer review record

Record the review in `checklist.md` or `changelog.md`:

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| `@[handle]` | `YYYY-MM-DD` | `[summary]` | `[none or list]` | Approved/Changes Required |

If no external reviewer is available, set Reviewer to `Self-review`, record the
date and result, and set Approval Status to `Needs independent review`. A
self-reviewed objective is not equivalent to independent approval.

The objective is complete only when its study guide, checklist, changelog,
cards, and generated TSV files pass this review together.
