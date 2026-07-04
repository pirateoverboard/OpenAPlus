# Objective 5.4 - Troubleshooting Mobile Devices

Objective 5.4 focuses on mobile-device symptoms and the technician decisions
that keep the device, user data, and user safe. Treat the device as a complete
support environment: battery, charging path, radios, storage, applications,
screen input, malware risk, accessories, and physical damage can all affect the
reported symptom.

## Battery and Charging Symptoms

Battery complaints need a quick split between normal battery aging, high power
usage, poor signal, and physical battery danger. A device with poor battery
health may need a battery replacement, but a device that is constantly searching
for signal or running a power-hungry app may first need a configuration or usage
check. Review app battery usage when the drain appears tied to a recent app or
usage change.

A swollen battery is a safety issue. Stop using the device, do not open the
battery pack, and follow proper replacement and disposal procedures. Treat this
differently from ordinary short runtime.

Charging symptoms should be isolated through the charging path. Inspect the
device port for debris or damage, avoid damaged cables, try a known-good cable,
and verify the power adapter before assuming the phone or tablet is failed.

## Physical Damage and Liquid Exposure

A broken screen is also a data-protection issue. Back up user data first if the
device is still usable, then arrange screen repair. Sharp glass can injure the
user or technician, so do not treat it as only a cosmetic problem.

Liquid exposure requires stopping normal troubleshooting. Power down the device,
do not charge it, do not keep pressing keys, and avoid heat. Remove removable
items such as the case, cards, back cover, or battery only when the device
design allows it. A Liquid Contact Indicator can support the damage history, but
it does not make the device safe to power on.

Damaged ports often show up as charging or data-transfer failures. If the port
is visibly damaged and known-good charging parts do not help, document the
evidence and escalate for hardware repair or replacement.

## Connectivity and Overheating

Mobile connectivity problems depend heavily on location. Poor cellular signal
may improve outdoors or in another area, while poor Wi-Fi may involve range,
interference, or channel/frequency conditions. Do not turn a single weak-signal
location into an unsupported device-failure diagnosis.

Overheating can be caused by battery activity, processor load, display
brightness, app behavior, or environmental heat. Ask what the device was doing
when it became hot, check app usage, and remove it from direct sunlight before
assuming an internal hardware failure.

## Touch, Stylus, and Input Problems

Digitizer and touchscreen symptoms include presses not registering, a black or
unresponsive screen, or input moving without the user touching the screen. A
restart can be a reasonable first isolation step for a frozen mobile interface.
Cursor drift or phantom input may require touch calibration if the platform and
device support it.

Stylus issues should be split into power, pairing, physical tip wear, and device
state. Check the stylus battery or charge first when the accessory is powered,
then verify Bluetooth pairing if the stylus depends on it.

## Apps, Malware, and Performance

App installation failures commonly point to storage, network access, OS/app
compatibility, store cache where applicable, or account credentials. Check one
of those conditions based on the observed symptom instead of reinstalling the
device.

Mobile malware can appear as unusual apps, pop-ups, unexpected data transfer,
high CPU usage, overheating, or unusual battery drain. Use an approved security
scanner or security app when symptoms suggest infection, and document user
impact before escalation.

Degraded performance can come from outdated software, low storage, excessive
background apps, hardware limitations, or hardware faults. Start with reversible
checks such as updates, restart, storage cleanup, and closing background apps
before escalating for replacement.

## Interview-ready Troubleshooting Language

For an interview, answer mobile-device tickets by showing safety, data
protection, and isolation. A strong pattern is:

"I would first confirm the symptom, when it started, and whether there was a
recent drop, liquid exposure, app install, OS update, or charging accessory
change. I would protect user data where possible, stop immediately for swollen
battery or liquid-exposure risks, then test one likely cause at a time with
least-invasive checks such as battery usage, storage, signal location, known-good
charging parts, restart, or app compatibility. I would document the symptom,
tests, results, user data status, and escalation reason."

Use the objective-local `interview/` directory for longer spoken-answer
practice. Regular Anki cards stay atomic: one symptom, one check, one
interpretation, or one escalation detail.

## References

- Professor Messer 220-1201 v1.70 p.53
- Professor Messer 220-1201 v1.70 p.54
- CompTIA 220-1201 Exam Objectives v2.0, Objective 5.4
