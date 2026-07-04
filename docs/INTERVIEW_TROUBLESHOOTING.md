# Interview troubleshooting practice

OpenAPlus can include interview-practice material for troubleshooting-heavy
objectives. This material helps learners explain a support process out loud,
but it is not a substitute for regular Anki cards.

Use interview practice for broad, multi-step questions that would make poor
flashcards. Keep regular Anki cards atomic: one symptom, cause, check, decision,
next step, or troubleshooting clue.

## Where it belongs

Put interview-practice material in an objective-local `interview/` directory:

```text
content/comptia/aplus/<exam>/<objective-slug>/interview/
```

Use consistent file names when possible:

```text
interview-scenarios.md
interview-answer-bank.md
```

Interview files are Markdown study material. They are not exported to normal
Basic, Cloze, or Image TSV output unless the pipeline is intentionally changed
to support that later.

## What interview practice is for

Use interview material for:

- common help desk interview questions;
- structured answer examples;
- troubleshooting talk tracks;
- what to say first;
- what information to gather;
- how to explain the reasoning;
- what to document;
- when to escalate; and
- mistakes to avoid.

Keep every scenario tied to the objective. Do not turn objective content into a
general resume, job-search, or workplace advice document.

## Interview versus Anki

| Material | Best for | Answer shape |
| --- | --- | --- |
| Regular Anki Basic card | One specific check, cause, decision, or clue | Short answer, usually under 15-20 seconds |
| Cloze card | One compact fact worth memorizing | One hidden term, acronym, value, or phrase |
| Image card | One visual recognition task | One visible target or symptom |
| Interview practice | Explaining a full troubleshooting approach | Multi-step spoken answer |

If a prompt asks "How would you troubleshoot this ticket?", it probably belongs
in interview practice. If it asks "What is the first thing to check?", it may be
a good Basic card if the answer is specific and source-backed.

## Recommended structure

An interview scenario should usually include:

```markdown
## Scenario: <short name>

Question:
<one interview-style prompt>

Strong answer pattern:
<a concise multi-step answer in the learner's voice>

What to say first:
<the first sentence or priority>

Information to gather:
- <specific fact>
- <specific fact>

Reasoning:
<why the order makes sense>

What to document:
- <symptom>
- <test result>
- <next step or escalation detail>

When to escalate:
<clear escalation trigger>

Mistakes to avoid:
- <unsafe assumption>
- <unsupported fix>
```

Use only the sections that add value. Do not pad every scenario to this full
shape if the objective needs something shorter.

## Good answer patterns

Strong interview answers usually show this order:

1. Gather the symptom and scope.
2. Check simple, safe causes before invasive fixes.
3. Form one theory from evidence.
4. Test one theory at a time.
5. Protect user data and safety where relevant.
6. Verify the result.
7. Document findings, actions, and outcomes.
8. Escalate with clear evidence when needed.

Use first-person phrasing where it helps the learner practice speaking:

```text
I would first confirm the exact symptom and whether it affects one user, one
device, or multiple devices. Then I would check simple causes before replacing
hardware. I would document each test result and escalate with the evidence if
the issue points beyond my support scope.
```

## Bad, okay, and great examples

| Situation | Bad | Why it is bad | Okay | Why it is only okay | Great | Why it is great |
| --- | --- | --- | --- | --- | --- | --- |
| Slow computer | "I would check everything and reinstall Windows." | It is vague, disruptive, and skips evidence. | "I would check Task Manager and startup apps." | It names useful checks but sounds tool-driven and incomplete. | "I would ask when it started, whether one app or the whole system is slow, and what changed. Then I would check resource pressure, startup impact, disk space, updates, and thermal symptoms one theory at a time." | It gathers scope, starts with low-risk checks, and explains the process. |
| Clicking drive | "I would run repairs and replace the drive." | It risks data loss and jumps to a fix. | "I would back up the data and check the drive." | It has the right priority but little detail. | "I would treat user data as the priority, avoid write-heavy repair attempts, confirm whether backups exist, document the symptom, and escalate or preserve the data according to policy before invasive work." | It shows risk awareness and escalation judgment. |
| Blank monitor | "I would replace the monitor." | It assumes the failed component. | "I would check cables and drivers." | It includes plausible checks but mixes layers without a sequence. | "I would confirm power, brightness, input source, and cable seating first. Then I would use a known-good display or computer to see whether the symptom follows the monitor, cable, port, or computer." | It uses simple checks first and explains the isolation test. |
| Boot device not found | "The drive is bad." | It turns one symptom into an unsupported diagnosis. | "I would check if the drive is detected." | This is a good first decision but not a full interview answer. | "I would record the exact boot error, check whether firmware detects the drive, verify boot order or removable media, and avoid repair steps that risk data until I know whether the drive is present and readable." | It separates detection, boot order, and data-risk decisions. |
| Network outage | "I would restart the router." | It may affect other users and lacks scope. | "I would see if other users are affected." | Good start, but not enough for a full response. | "I would verify whether the issue affects one user, one device, one network area, or everyone. That scope decides whether I focus on the endpoint, local connection, wireless segment, or upstream service before making changes." | It explains why scope controls the troubleshooting path. |

## Converting broad cards into interview material

Move a card out of regular Anki and into `interview/` when it:

- asks for a full troubleshooting process;
- contains several symptoms at once;
- expects several unrelated checks;
- has a long multi-step answer;
- feels like spoken interview response practice;
- takes more than about 15-20 seconds to answer; or
- uses "how would you troubleshoot" as the core prompt.

After moving the broad target, replace the regular card with smaller cards such
as:

- one symptom recognition card;
- one most-likely-cause card;
- one first-check card;
- one safest-next-step card;
- one known-good-test interpretation card;
- one user-question card;
- one documentation card; or
- one escalation-trigger card.

## Source and copyright rules

Interview material must follow the same source rules as cards and study guides:

- use the CompTIA objective as the scope authority;
- validate against approved references;
- cite source pages or objective references where useful;
- paraphrase heavily;
- do not copy source wording, tables, diagrams, screenshots, or layouts; and
- record ambiguity instead of inventing unsupported troubleshooting steps.

Interview examples may be original, but their technical claims still need to be
source-backed and objective-scoped.

## Review checklist

Before accepting interview-practice material, confirm:

- [ ] It is stored under the objective's `interview/` directory.
- [ ] It is tied to the current objective.
- [ ] It does not duplicate long answer blocks in `study-guide.md`.
- [ ] It does not appear in generated TSV output.
- [ ] It contains realistic support-language practice.
- [ ] It avoids unsupported vendor-specific fixes.
- [ ] It preserves data-protection, safety, verification, documentation, and
      escalation reasoning where relevant.
- [ ] Any broad regular Anki cards were split into atomic review cards.
- [ ] `checklist.md` and `changelog.md` record the interview material and any
      card splits.
