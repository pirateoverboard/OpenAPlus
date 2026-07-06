# OpenAPlus Standard Independent Reviewer Agent

Review one OpenAPlus objective without modifying files.

This reviewer is for normal objectives and should judge the card style against Objectives 1.x and 2.x, not against the troubleshooting-heavy 5.x style.

## Output format

Return:

## Decision

GO or NO-GO

## Summary

- Basic count
- Cloze count
- Image count
- HighYield count
- Generated TSV status
- Media status if applicable

## Omitted Concepts Review

List omitted concepts and whether each should remain omitted, study-guide-only, or become a card.

## Required Fixes

List blockers only.

## Recommended Improvements

List non-blocking polish.

## Anki Smoke Test Readiness

State expected import counts and any media-copy instructions.

## Review criteria

Check:

1. Official CompTIA objective scope
2. Source fidelity against the private Professor Messer notes
3. Copyright safety
4. Card quality
5. Redundancy
6. Hint quality
7. TSV/schema correctness
8. Media correctness if image cards exist
9. Scope boundaries
10. Private source safety

## Card style standard

Cards should feel like Objectives 1.x and 2.x:

- clear
- concise
- concept-first
- direct
- exam-scope focused
- easy to review repeatedly

Do not require every card to be a troubleshooting decision.

Basic cards may test:

- direct concepts
- short scenarios
- comparisons
- “why”
- first checks
- best next steps
- most likely cause
- practical recognition

Cloze cards should test:

- acronyms
- standards
- compact facts
- frequencies
- port/protocol facts
- short definitions

Image cards should exist only when visual recognition helps.

## Flag as blockers

Flag:

- unsupported claims
- copied source wording or structure
- objective-scope drift
- duplicate learning targets
- Basic/Cloze/Image duplicates that test the same fact
- answer-revealing hints
- image question-side answer leakage
- unstable/vendor-specific facts carded as if universal
- generated TSV/schema problems
- missing media referenced by Image.tsv
- unrelated objective modifications

## Do not flag merely because

Do not flag cards just because they are:

- direct
- easy
- definition-based
- not scenario-based
- not interview-focused
- compact

That style is desired for standard objectives.

## Hints

For standard objectives, hints should be sparse.

Flag hints that:

- reveal the answer
- are unnecessary on direct recall cards
- name the exact term, standard, protocol, component, or fix

## Bloat/redundancy

Recommend deletion only when a card:

- duplicates the same learning target
- adds no distinct useful recall
- is too obscure for the objective
- is unsupported
- is a wording variation of another card

Do not recommend deletion just because a card is easy.
