# Objective 5.3 - Troubleshooting Display Issues

Objective 5.3 focuses on display symptoms and the evidence that separates a
simple setup issue from a cable, monitor, projector, driver, operating system,
or graphics-adapter problem. A strong help desk answer starts with the visible
symptom, checks simple noninvasive causes, then uses known-good swaps and
configuration checks to narrow where the problem follows.

## No image or incorrect input

A blank screen is not automatically a failed monitor. First confirm power,
signal cabling, the selected input, brightness, and whether the computer is
actually producing video. If those checks do not explain the symptom, test with
a known-good cable, port, or display to see whether the issue follows the
monitor path or the computer.

If video appears before the operating system loads but disappears afterward,
separate firmware/POST video from operating-system display settings or drivers.
Use a low-resolution or recovery display path when supported before replacing
hardware.

## Fuzzy, distorted, flashing, or incorrectly sized image

Fuzzy images and incorrect sizing often point to a mismatch between the system
output and the display. Check resolution, refresh rate, scaling, and the
display's native resolution before assuming the panel is damaged.

Flashing, intermittent signal loss, color patterns, missing colors, or visible
artifacts can be caused by loose cabling, damaged pins, a bad cable, a failing
display, a graphics adapter problem, or a driver/configuration issue. The
support goal is to choose the least invasive test that separates those paths.

## Incorrect color and dim image

Incorrect colors may come from display presets, tint settings, operating-system
color modes, driver configuration, cable/pin problems, or a failing component.
Ask when the color changed and whether it affects one display, one cable path,
or all outputs.

A dim image should be checked in layers: monitor brightness and contrast, OS
auto-dimming or battery settings, then backlight failure if the image exists but
the lighting is missing or uneven. Do not replace the display before ruling out
settings that can make a working display look dim.

## Projector and audio symptoms

Projectors add heat, lamp, airflow, and cooldown behavior to the troubleshooting
path. A projector that shuts down or loses brightness may need airflow checks,
filter cleaning, cooldown time, or bulb replacement rather than computer
repair.

Monitors and projectors may also carry audio over the same connection used for
video, such as HDMI, DisplayPort, or Thunderbolt. For display-audio complaints,
check mute and volume controls, the selected audio output in the OS, and whether
the display expects audio through the video cable or a separate input.

## Permanent display defects

Burn-in, image sticking, dead pixels, and cracked or damaged panels should be
distinguished from cable or operating-system issues. Some temporary image
retention may improve, but dead pixels and physical panel damage are usually
handled through replacement, warranty, or escalation.

## Interview-ready troubleshooting language

For longer spoken-answer practice, see
`interview/interview-scenarios.md` and `interview/interview-answer-bank.md`.
Those files hold broad troubleshooting talk tracks that are intentionally not
exported as regular Anki cards.

- "I would first confirm whether the issue follows the display, the cable, the
  port, or the computer."
- "I would check power, input source, brightness, and cable seating before
  replacing a monitor."
- "If video works before the OS loads but fails afterward, I would look at
  display settings or drivers before assuming the monitor failed."
- "For flashing or artifact issues, I would try a known-good cable and display
  path to separate cable, panel, adapter, and driver causes."
- "For a projector, I would include bulb life, airflow, filters, and cooldown
  behavior in the troubleshooting notes."
- "I would document the symptom, when it started, tested cable/port/display,
  OS settings checked, and the result before escalating."

## References

- CompTIA 220-1201 Exam Objectives v2.0, Objective 5.3
- Professor Messer 220-1201 v1.70 p.52
- Professor Messer 220-1201 v1.70 p.53
