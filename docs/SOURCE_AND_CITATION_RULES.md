# Source and citation rules

Every OpenAPlus fact must be supported. If a claim cannot be verified, do not
publish it.

## Source roles

- CompTIA exam objectives define what is in scope.
- Professor Messer course notes for the matching exam version are the preferred
  authoring reference.
- Professor Messer videos and official vendor documentation may clarify details.

Explanatory detail may be added only when it supports an in-scope objective.
Out-of-scope detail must not become a flashcard unless a reviewer explicitly
approves it as concise `Tech Wisdom` in Instructor Notes. Confirm that every
source matches the exam version being authored.

## Card citations

Every card requires a non-empty YAML `source` list. Each entry should let a
reviewer locate the material, including version, page, video timestamp, section,
or vendor document identifier when available.

```yaml
source:
  - Professor Messer course notes, <exam/version>, p. <page>
  - Vendor documentation, <document title>, <section>
```

The angle-bracketed values are placeholders, not citations to copy verbatim.

## Study-guide references

Every study guide must end with a `## References` section. Use concise entries:

```markdown
## References

- Professor Messer 220-1201 v1.70 p.1
- CompTIA 220-1201 Exam Objectives, Objective 1.1
- Vendor documentation, product/topic name
```

Study guides must paraphrase. Do not reproduce long passages, transcripts, or
source-specific organization.

## Copyright and original work

- Paraphrase educational content in original language.
- Write original explanations rather than lightly rewriting a source.
- Create original diagrams only. Do not copy, trace, screenshot, or adapt
  copyrighted diagrams.
- Never contribute exam dumps, recalled exam questions, or proprietary study
  material.

A citation establishes provenance; it does not grant permission to copy.

## Ambiguous sources

When approved sources conflict or remain ambiguous:

1. Do not guess or create a card from the uncertain claim.
2. Record the source, question, and affected concept in the objective's
   `changelog.md`.
3. Ask a maintainer or subject-matter reviewer for clarification.
4. Resume authoring only after the decision and supporting source are recorded.
