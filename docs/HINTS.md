# Hint authoring guide

Hints are optional, learner-facing guidance shown before answer reveal. A good
hint helps the learner choose a troubleshooting path without doing the recall
for them.

Use a Hint when it improves reasoning before reveal. Remove the Hint if the only
useful hint would reveal the answer.

## How hints are used

OpenAPlus Basic cards have a stable `Hint` TSV field between `Front` and `Back`.
Cards may omit the source `## Hint` section; the generated TSV still includes an
empty Hint field. The OpenAPlus Basic note type can then use one field mapping
for every Basic TSV.

Hints appear before reveal. Instructor Notes appear after reveal. This means a
Hint should nudge the learner toward a decision process, while Instructor Notes
should explain why the answer is correct after the learner commits.

Hints are especially useful for troubleshooting objectives 5.1 through 5.6,
where learners need to reason through symptoms, risk, scope, and next steps.
They are less useful for direct recall cards where any meaningful hint would
name the answer.

## Hint rules

- Keep hints short, usually one sentence.
- Guide reasoning, not memorized wording.
- Point to the kind of evidence, risk, or decision order that matters.
- Do not name the exact answer, exact tool, exact fix, likely cause, or
  technology unless the question already names it.
- Do not add a hint just to fill the field.
- Keep deeper explanation in Instructor Notes.

## Hint versus Instructor Notes

| Field | Timing | Purpose | Good use |
| --- | --- | --- | --- |
| Hint | Before reveal | Steer the learner's reasoning without revealing the answer | "Start with simple physical and configuration checks." |
| Instructor Notes | After reveal | Explain the troubleshooting logic, trap, or real support relevance | "A moved desktop increases the chance of a loose cable, so cabling is checked before replacement." |

## Examples

| Card situation | Bad hint | Why it is bad | Okay hint | Why it is only okay | Great hint | Why it is great |
| --- | --- | --- | --- | --- | --- | --- |
| Storage health warning | "Check S.M.A.R.T." | It names the tool and likely answer. | "Look at health data." | Directionally useful but vague. | "Treat health warnings as a chance to act before users lose access." | It guides urgency and reasoning without naming the exact step. |
| DHCP-style addressing issue | "This is probably DHCP." | It gives away the likely answer. | "Think about IP assignment." | It helps, but still points tightly at the answer. | "Check whether the device received the expected configuration automatically." | It frames the decision without naming the service. |
| Failing drive with user data | "Replace the drive." | It gives a fix and skips data protection. | "The drive may be failing." | It names the likely cause too directly. | "Protect user data before attempting risky repair." | It teaches the priority without revealing the final action wording. |
| Slow computer triage | "Use Task Manager." | It names the exact tool. | "Check resource usage." | Useful, but close to the answer if the card asks for a tool. | "Start with a quick way to measure which resource is under pressure." | It points to measurement without naming the tool. |
| APIPA symptom | "Think about APIPA." | It repeats the symptom/technology instead of guiding reasoning. | "Think about automatic addressing." | Better, but still close to the target. | "Compare the observed address with the configuration the client expected." | It encourages diagnosis from evidence. |
| Hostname failure | "The issue is DNS." | It gives away the answer. | "Think about name resolution." | It is often too revealing for a DNS card. | "Compare what works by address with what fails by name." | It gives a reasoning test rather than the answer. |
| Unknown hardware symptom | "Replace hardware." | It jumps to an invasive fix. | "Gather more information." | True, but generic. | "Look for evidence before replacing hardware." | It reinforces a useful support principle. |
| Intermittent issue | "Ask what changed." | Useful but narrow. | "Think about recent changes and scope." | Good but slightly broad. | "Think about what changed and what scope the issue affects." | It guides interview-style triage without naming a cause. |
| Boot/storage issue | "The drive failed." | It states the likely cause. | "Check the drive." | Too close to the answer and vague. | "Confirm whether the device is detected before assuming failure." | It teaches a decision split without revealing the fix. |
| Hardware replacement decision | "Swap the part." | It gives the action. | "Try a test first." | Useful but vague. | "Choose the least invasive test that can confirm your theory." | It guides safe troubleshooting order. |

## Self-review checklist

- Does the hint help before reveal?
- Could a learner answer the card correctly from the hint alone? If yes, remove
  or rewrite it.
- Is the hint shorter and less explanatory than Instructor Notes?
- Does the hint avoid naming the exact answer, tool, fix, likely cause, or
  technology?
- Would the card still be fair if the hint were omitted? If not, the question
  may need better wording instead of a stronger hint.
