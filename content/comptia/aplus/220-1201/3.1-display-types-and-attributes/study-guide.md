# Objective 3.1: Display Types and Attributes

Objective 3.1 covers display panel technologies, touch input hardware, display
lighting, and the attributes a technician uses to match a display to a workload.
The useful skill is recognizing the hardware tradeoff, not memorizing every
marketing name or every possible resolution.

## Display panel types

An **LCD** uses liquid crystals to control light. Because the crystals do not
produce their own light, an LCD needs a separate backlight. That design keeps
LCDs common and relatively efficient, but dark scenes depend on how well the
backlight can be controlled.

**Mini LED** is still an LCD backlight approach. It uses many smaller LEDs so
the display can control smaller lighting zones. This can improve dark areas and
color behavior compared with a simpler backlight, but it does not make the panel
an OLED.

**OLED** pixels emit light themselves. Because a separate backlight is not
required, OLED panels can be thinner and are common in mobile devices and
premium displays. They are useful when accurate color and dark-area control are
important, but cost may be higher than LCD options.

## LCD panel technologies

**TN** panels are associated with fast response. The tradeoff is weaker viewing
angles and visible color shift when viewed off-axis.

**IPS** panels are associated with strong color representation. They are a good
fit for color-sensitive work, though they may cost more to produce than TN.

**VA** panels sit between TN and IPS for many use cases. They can provide good
color behavior, but response time may be slower than TN.

## Touch and pen input

A **touchscreen** combines display output with direct touch input. It is useful
for tablets, hybrid systems, and any workflow where finger input is preferable
to a separate keyboard or pointer.

A **digitizer** supports pen or stylus input. This matters for sketching,
annotation, signatures, or other work where precise pen-like control is the
reason for choosing the device.

## Backlight and inverter troubleshooting

LCD systems need a light source behind the panel. Some systems also use an
inverter to provide the electrical output needed by the display lighting. A very
dim image that can only be seen with close inspection or a flashlight points the
technician toward the display lighting path rather than immediately toward the
graphics adapter.

## Display attributes

**Pixel density** describes how many pixels fit into a physical measurement,
often pixels per inch. Two displays can have the same resolution but different
sharpness if their physical sizes differ.

**Refresh rate** describes how frequently the display can update the image,
usually in hertz. Higher refresh rates matter most for rapid motion, such as
games, sports, and video production. The display, graphics hardware, and cable
connection all have to support the required mode.

**Resolution** is the pixel count across the width and height of the image. More
pixels can provide a clearer image, but the final experience also depends on
physical size, scaling, and viewing distance.

**Color gamut** is the range of colors a display can represent. Color-sensitive
work should consider gamut support and coverage of the relevant standard rather
than choosing a display only by size or resolution.

## Intentionally limited detail

OpenAPlus does not card exact display dimensions, every named resolution,
current HDMI or DisplayPort mode tables, vendor-specific panel marketing,
product model claims, or exact laptop disassembly procedures here. Those details
are volatile, implementation specific, or covered more appropriately in cable
and troubleshooting objectives.

## References

- CompTIA 220-1201 Exam Objectives v2.0, Objective 3.1
- Professor Messer 220-1201 v1.70 p.21
- Professor Messer 220-1201 v1.70 p.22
