# Card authoring guide

Choose the card type that matches the learner's task. Do not force every concept
into every card type.

## Card types

### Basic

Use Basic cards for application and judgment: scenarios, troubleshooting,
comparisons, causes, consequences, “why,” and ordered decisions.

**Good:** “A system shows `[symptom]` after `[change]`. What is the FIRST thing
to check?” The answer gives one sourced initial check and explains why it comes
first.

**Bad:** “List everything about `[topic]`.” The scope and expected answer are
undefined.

Basic cards may include an optional `## Hint` section when a pre-reveal nudge
improves reasoning without giving away the answer. See [HINTS.md](HINTS.md).

### Cloze

Use Cloze cards for compact recall: a definition, acronym, command, port,
standard, or other short fact. See [CLOZE_GUIDE.md](CLOZE_GUIDE.md).

**Good:** “`[acronym]` stands for {{c1::[expansion]}}.”

**Bad:** A paragraph with many unrelated deletions. It tests reconstruction of
the sentence rather than useful recall.

### Image

Use Image cards when recognizing a visual feature is the learning task. See
[IMAGE_CARD_GUIDE.md](IMAGE_CARD_GUIDE.md).

**Good:** A clean original diagram that masks one labeled component on the
question image and reveals it on the answer image.

**Bad:** A decorative image that contributes nothing to answering the prompt.

## Atomic cards

An atomic card has one retrieval target. A learner should know what a complete
answer contains before revealing it.

**Good:** “What is the primary purpose of `[single term]`?”

**Bad:** “Define `[term A]`, `[term B]`, and `[term C]`, compare them, and give
two examples of each.” Split this into independently reviewable cards.

Avoid multi-answer cards unless the exam explicitly expects a fixed list. When
a list is required, state its size and boundary: “Name the three `[items]`
specified by `[source scope]`.” Preserve the source's ordering only when order
matters.

## Scenario cards

A scenario should contain only details needed to choose the answer:

1. Establish the relevant environment or constraint.
2. State one observable symptom or goal.
3. Ask for one action, cause, or conclusion.
4. Put the reasoning—not extra ambiguity—in Instructor Notes.

Do not add irrelevant narrative merely to make a recall question look applied.
Use hints sparingly for scenario cards: they should guide the learner toward the
right troubleshooting process, not name the tool, cause, or fix.

Longer "how would you troubleshoot this ticket?" prompts are interview-practice
material, not regular Anki cards. Put those broader spoken-answer exercises in
the objective's `interview/` directory and follow
[INTERVIEW_TROUBLESHOOTING.md](INTERVIEW_TROUBLESHOOTING.md). Then split the
regular Anki coverage into atomic cards with one symptom, check, decision, or
troubleshooting clue.

## Calibrated decision wording

Use **MOST likely**, **BEST next step**, and **FIRST thing to check** only when
the source and scenario establish a unique ranking:

- **MOST likely** asks for the highest-probability explanation under the stated
  evidence, not every possible cause.
- **BEST next step** asks for the most appropriate action after the stated work
  is already complete.
- **FIRST thing to check** asks for the earliest justified check, usually based
  on order of operations, safety, speed, or least disruption.

If two answers remain equally defensible, add the missing constraint or rewrite
the card. Never use superlative wording to hide ambiguity.
