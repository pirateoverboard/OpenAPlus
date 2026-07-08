# Source and citation rules

Every OpenAPlus fact must be supported. If a claim cannot be verified, do not
publish it.

## Source roles

- Official CompTIA A+ objective PDFs are the primary scope authority. They
  define objective boundaries, objective titles, bullet scope, and what must be
  covered.
- Professor Messer PDFs are the approved secondary validation/page-reference
  source after the official CompTIA objective establishes scope.
- Professor Messer practice exam PDFs are approved private secondary gap-check
  sources after official scope is established. They must not define objective
  scope and must not be used as the source for copied or lightly rewritten
  practice questions, answer choices, or explanations.
- Professor Messer videos, vendor documentation, and any other secondary source
  require explicit user approval unless that source has already been approved
  for the objective being authored or reviewed.

Explanatory detail may be added only when it supports an in-scope objective.
Out-of-scope detail must not become a flashcard unless a reviewer explicitly
approves it as concise `Tech Wisdom` in Instructor Notes. Confirm that every
source matches the exam version being authored.

Authoring source hierarchy:

1. Official CompTIA exam objectives PDF determines objective scope.
2. Professor Messer PDFs validate concepts and page references.
3. Professor Messer practice exam PDFs may be used only as private secondary
   gap-check sources for concepts already supported by the official objective
   scope and approved validation sources.
4. OpenAPlus content must be original, paraphrased, objective-scoped, and
   learner-focused.

Private local paths:

- Core 1 official objectives:
  `~/openaplus-private-sources/comptia-a-plus-220-1201-exam-objectives-v4.0.pdf`
- Core 2 official objectives:
  `~/openaplus-private-sources/comptia-a-plus-220-1202-exam-objectives-v4.0.pdf`
- Professor Messer Core 1 notes:
  `~/openaplus-private-sources/professor-messer-comptia-220-1201-a-plus-course-notes-v170.pdf`
- Professor Messer Core 2 notes:
  `~/openaplus-private-sources/professor-messer-comptia-220-1202-a-plus-course-notes-v140.pdf`
- Professor Messer Core 1 practice exams:
  `~/openaplus-private-sources/professor-messer-a-plus-220-1201-core-1-practice-exams-v112.pdf`
- Professor Messer Core 2 practice exams:
  `~/openaplus-private-sources/professor-messer-a-plus-220-1202-core-2-practice-exams-v111.pdf`

## Practice exam handling

Practice exam PDFs are private gap-check sources only.

- Do not copy, paraphrase closely, or reconstruct practice-test questions,
  answer choices, rationales, or scenarios.
- Do not create a card solely because a concept appears in a practice exam; the
  concept must also be inside official objective scope and supported by an
  approved validation/reference source.
- Use practice exams to identify possible coverage gaps, ambiguity, or weak
  distractor distinctions, then resolve those items against the official
  objectives and approved notes.
- When a matching practice exam is available, perform this gap check before
  objective acceptance. If it surfaces an official-scope, source-supported,
  stable concept that is useful for active recall or application, create an
  Anki card by default. Leaving that concept study-guide-only requires a
  specific no-card reason in the objective checklist.
- Do not cite practice exams in card metadata or study-guide references. When
  useful for review provenance, record practice-exam use only in checklist or
  changelog notes without enough detail to reconstruct a question.

## Card citations

Every card requires a non-empty YAML `source` list. Each entry should let a
reviewer locate the material, including official objective number, version, page,
section, or approved document identifier when available.

```yaml
source:
  - CompTIA 220-1201 Exam Objectives v4.0, Objective <objective>
  - Professor Messer course notes, <exam/version>, p. <page>
```

The angle-bracketed values are placeholders, not citations to copy verbatim.

## Study-guide references

Every study guide must end with a `## References` section. Use concise entries:

```markdown
## References

- Professor Messer 220-1201 v1.70 p.1
- CompTIA 220-1201 Exam Objectives, Objective 1.1
```

Study guides must paraphrase. Do not reproduce long passages, transcripts, or
source-specific organization.

## Copyright and original work

- Paraphrase educational content in original language.
- Write original explanations rather than lightly rewriting a source.
- Create original diagrams or use only reviewed external images allowed by the
  image-source policy. Do not copy, trace, screenshot, or adapt copyrighted
  diagrams.
- Do not commit official CompTIA PDFs, Professor Messer PDFs, practice exam
  PDFs, screenshots, OCR exports, copied tables, copied diagrams, copied source
  layouts, practice questions, answer choices, explanations, or long copied
  passages.
- Never contribute exam dumps, recalled exam questions, or proprietary study
  material.

A citation establishes provenance; it does not grant permission to copy.

## Ambiguous sources

When approved sources conflict or remain ambiguous:

1. Do not guess or create a card from the uncertain claim.
2. Record the source, question, and affected concept in the objective's
   `checklist.md`.
3. Ask a maintainer or subject-matter reviewer for clarification.
4. Mention the ambiguity in `changelog.md` only when it affects review,
   acceptance, or a material coverage decision.
5. Resume authoring only after the decision and supporting source are recorded.
