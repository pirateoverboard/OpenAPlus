# Objective 5.1 interview scenarios

Use these prompts for spoken troubleshooting practice. They are intentionally
longer than regular Anki cards and are not exported to TSV output.

## Slow computer

Question:
A user says their computer is running slowly. How would you troubleshoot it?

Answer pattern:
I would first ask when the slowdown started, whether it affects one app or the
whole system, whether anything recently changed, and whether the issue happens
on AC power, battery power, startup, or under load. Then I would check simple
evidence first, such as Task Manager resource use, startup activity, disk
activity, power-saving mode, updates, and obvious thermal symptoms. I would test
one theory at a time, verify improvement, and document the symptoms, checks,
and results.

Mistakes to avoid:
- Do not replace memory, CPU, or storage before checking resource evidence.
- Do not ignore whether the issue is app-specific or system-wide.
- Do not skip recent-change questions.

## Blue screen after a recent change

Question:
A workstation starts blue-screening after a driver or hardware change. What
would you do?

Answer pattern:
I would record the exact message or screenshot, ask what changed and when, and
check whether the crash happens during startup or only during certain work. If a
driver change is the strongest clue, I would use a reversible recovery path such
as Safe Mode, driver rollback, System Restore, or an approved recovery method
before replacing hardware. If I could not resolve it, I would escalate with the
error, timing, recent changes, logs, diagnostics, and steps already tested.

Mistakes to avoid:
- Do not reinstall Windows as the first response.
- Do not discard the stop message or screenshot.
- Do not treat every crash as hardware failure.

## No power

Question:
A desktop shows no lights, no fans, and no response. How would you start?

Answer pattern:
I would begin outside the computer and follow the power path inward: outlet,
power strip, power cable, adapter if present, and power supply input. If there
is still no response, I would check approved internal power connections or power
supply output according to policy. I would avoid replacing the motherboard until
I had evidence that power is reaching the system correctly.

Mistakes to avoid:
- Do not open the system before checking the external power path.
- Do not assume the motherboard failed from a no-response symptom alone.
- Do not keep testing if there is smoke or a burning smell.

## Random shutdowns under load

Question:
A PC shuts down during video rendering or gaming but works at the desktop. What
would you check?

Answer pattern:
I would use the load pattern as evidence. I would check temperatures, fan
operation, airflow, dust blockage, heat sinks, and event logs or diagnostics.
If the system remains unstable, I would document the load condition, thermal
evidence, diagnostics, and any hardware symptoms before escalating.

Mistakes to avoid:
- Do not assume the graphics card is bad without thermal or diagnostic evidence.
- Do not ignore blocked airflow or failed fans.
- Do not continue stress testing if there is a safety concern.

## Escalation

Question:
You cannot resolve an intermittent hardware issue. What should your escalation
include?

Answer pattern:
I would document the user symptom, timing, frequency, recent changes, exact
error text or screenshots, Event Viewer or diagnostic details, hardware checks,
tests performed, and the result of each step. The goal is to let the next
technician continue from the evidence instead of starting the ticket over.
