# Objective 5.1 - Troubleshooting Hardware

Objective 5.1 focuses on recognizing common hardware symptoms and choosing a
systematic next action. For help desk work, the important skill is not guessing
the failed part immediately. Start by gathering symptoms, checking simple causes,
testing a reasonable theory, and documenting what changed after each step.

## POST and boot symptoms

POST checks major hardware before the operating system loads. A failure may show
as beeps, status codes, or a blank screen before boot. The exact meaning of a
beep or code depends on the system firmware or manufacturer, so a technician
should record the pattern and check the correct documentation instead of
memorizing generic beep-code tables.

Boot failures can also come from configuration or removable media. If a system
tries to start from the wrong device, check for inserted media, confirm the boot
order, and verify that the intended startup device contains a usable operating
system.

## Crash screens and shutdowns

A crash screen can include details that help narrow the fault. Record the exact
message, stop information, recent changes, and whether the symptom happens at
startup, shutdown, after a driver update, or only under load. Event logs and
manufacturer diagnostics can support the theory before parts are replaced.

If a blue screen begins after a driver or hardware change, use the least
disruptive recovery path first, such as Safe Mode, driver rollback, System
Restore, or Last Known Good-style recovery where available. A random black-screen
shutdown under load points more strongly toward heat or failing hardware, so
check temperatures, fans, heat sinks, recent changes, and diagnostic results.

Application crashes are narrower than whole-system crashes. Check application
messages, Event Viewer, and Reliability Monitor before reinstalling the
application or escalating to the application vendor.

## Display and power checks

A blank display does not prove the computer failed. First verify the monitor has
power, the signal cable is connected, the correct input is selected, and
brightness is not turned down. If the monitor remains suspect, swap the monitor
or test it on another computer.

For a no-power complaint, verify the power source before assuming the motherboard
or power supply is bad. Check the outlet, power strip, cable, adapter, and power
supply output where appropriate. If fans spin but the system does not POST, do
not treat the spinning fans as proof that all power rails are healthy; low-power
fans may run while other devices still lack correct power.

Smoke or a burning smell is a safety issue. Disconnect power and do not continue
testing until the damaged component is located and replaced. A computer should
not have a burned odor after it cools down.

## Performance and overheating

Sluggish performance should be narrowed with evidence. Start with Task Manager
or similar tools to check CPU use, memory pressure, disk I/O, and obvious runaway
processes. Also check free disk space, patch and driver status, malware
possibility, and laptop power-saving mode before replacing hardware.

Overheating often appears during sustained CPU or graphics load. Check for
blocked airflow, failed fans, dirty heat sinks, and poor cooling contact. BIOS or
monitoring software can help confirm the temperature trend, but use product
documentation and approved tools in a real support environment.

## Time, battery, and noise symptoms

A system that loses date, time, or firmware settings at every boot often points
to the motherboard battery. Replace the battery using the system service
procedure and then restore the correct date, time, and firmware settings.

Unusual noises are symptom clues. Rattling suggests something loose, scraping may
point toward a mechanical drive issue, clicking can be fan-related, and a popping
sound may indicate a failed component. Use the sound as a starting clue, then
confirm with inspection and diagnostics.

## Interview-ready troubleshooting language

For longer spoken-answer practice, see
`interview/interview-scenarios.md` and `interview/interview-answer-bank.md`.
Those files hold broad troubleshooting talk tracks that are intentionally not
exported as regular Anki cards.

- "I would first gather when the symptom started, what changed recently, and
  whether it affects one device or many devices."
- "I would check simple external causes first, such as power, cables, input
  selection, and removable media, before opening the system."
- "If the system gives a POST beep or code, I would record the exact pattern and
  check the correct manufacturer documentation instead of guessing."
- "For a blue screen after a driver change, I would try Safe Mode or driver
  rollback before replacing hardware."
- "For random shutdowns under load, I would look for heat evidence and fan
  status, then verify with logs or diagnostics."
- "Before escalating, I would document the user symptom, recent changes, exact
  messages, screenshots if available, tests performed, and results."
- "I would avoid replacing hardware until the evidence points to that component."

## References

- CompTIA 220-1201 Exam Objectives v2.0, Objective 5.1
- Professor Messer 220-1201 v1.70 p.48
- Professor Messer 220-1201 v1.70 p.49
- Professor Messer 220-1201 v1.70 p.50
