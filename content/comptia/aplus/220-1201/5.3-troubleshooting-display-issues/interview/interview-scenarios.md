# Objective 5.3 interview scenarios

Use these prompts for spoken troubleshooting practice. They are intentionally
longer than regular Anki cards and are not exported to TSV output.

## Intermittent monitor issue

Question:
A monitor sometimes flickers, sometimes shows wrong colors, and works normally
after moving to another desk. How would you troubleshoot it?

Answer pattern:
I would ask what changed and whether the symptom follows the monitor, cable,
port, dock, adapter, computer, or user location. Then I would start with simple
checks: power, input source, cable seating, brightness, and visible connector
damage. I would use known-good swaps to isolate the display path, then check
resolution, refresh rate, OS display settings, and driver behavior if the
hardware path looks stable. I would document what was tested and where the
symptom followed before escalating.

Mistakes to avoid:
- Do not replace the monitor just because it is the visible part.
- Do not reinstall drivers before checking movement-sensitive cabling.
- Do not ignore scope: one display path versus multiple displays.

## No signal after moving a desktop

Question:
A user moved a desktop and the monitor shows no signal. What would you do?

Answer pattern:
I would check the external display path first: monitor power, selected input,
video cable seating, brightness, and whether the computer appears to be
producing video. If those checks do not explain the symptom, I would test with a
known-good cable, port, or display to see whether the issue follows the monitor
path or the computer.

Mistakes to avoid:
- Do not assume the monitor failed before checking input and cable seating.
- Do not skip power or brightness because the computer is running.
- Do not treat a no-signal message as proof of operating-system failure.

## Projector shutdown

Question:
A conference-room projector works briefly, gets hot, and shuts down. How would
you handle it?

Answer pattern:
I would focus on projector-specific causes before blaming the laptop. I would
inspect airflow, fans, filters, vents, cooldown behavior, and bulb condition. I
would document the runtime before shutdown, temperature or warning indicators,
and maintenance condition before escalating or scheduling service.

Mistakes to avoid:
- Do not keep restarting an overheating projector.
- Do not blame the laptop when the symptom follows projector heat.
- Do not ignore filters, vents, or cooldown time.

## Faint laptop display

Question:
A laptop display is barely visible, but an external monitor works normally. How
would you explain your reasoning?

Answer pattern:
The external monitor shows that the computer can generate video. I would check
brightness, contrast, auto-dimming, battery or power settings, and driver
configuration first. If the image remains present but very faint, I would
suspect the built-in panel lighting path and escalate for display repair.

Mistakes to avoid:
- Do not replace the whole computer before separating video output from panel
  lighting.
- Do not ignore auto-dimming or battery settings.
- Do not promise board-level repair at the help desk.

## Display escalation

Question:
You need to escalate a display issue after basic checks and known-good tests.
What should your ticket include?

Answer pattern:
I would document the exact symptom, when it started, whether the issue follows
the display, cable, port, adapter, OS settings, or computer, which known-good
items were tested, driver or OS changes, and the current user impact. That lets
the next technician continue from evidence instead of repeating basic checks.
