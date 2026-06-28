# Objective 1.1: Laptop Hardware

Objective 1.1 focuses on recognizing laptop hardware, understanding how design
choices affect replacement, and selecting an appropriate action in a short
service scenario. Laptop components are compact and model-specific, so a method
that works on one system may require substantially different disassembly on
another.

## Scope Status

This objective is **not yet accepted as complete**. Two CompTIA scope items need
additional source or maintainer clarification:

- **Camera/webcam:** CompTIA Objective 1.1 v2.0 lists camera/webcam, while the
  supplied authoring scope omits it and the available private notes place that
  discussion with 1.2. No camera/webcam content is included here.
- **Wireless cards:** CompTIA uses this broad term, but the available private
  Objective 1.1 pages support antenna placement and general Wi-Fi/Bluetooth
  roles rather than a model-independent replacement procedure. No replacement
  procedure was invented.

These unresolved items and the pending Anki smoke test block production
acceptance; they do not expand this work into Objective 1.2.

## Repair Strategy

Begin with the service information for the exact laptop model. Identify whether
the target part is externally accessible, behind a service cover, or beneath a
larger assembly. Repair-time and screw-count examples are useful illustrations,
not universal procedures. (Professor Messer, p. 1)

## Batteries

A laptop battery supplies power while the computer is disconnected from an
external power source. Some batteries are modular and readily removable; others
are internal and require significant disassembly. Physical shape and connector
placement vary by model, so compatibility must be verified rather than inferred
from battery chemistry alone. (Professor Messer, p. 1)

Lithium-ion (Li-ion) and lithium-ion polymer (LiPo) are common laptop battery
technologies. They do not require a full-discharge routine to prevent the memory
effect associated with older battery technologies. Battery chemistry and
physical replacement design are separate considerations. (Professor Messer,
p. 1)

## Keyboard and Keys

A replaceable keyboard may be secured with screws and connected by a ribbon
cable, but the access procedure remains model-specific. When an internal
keyboard cannot be repaired immediately, an external USB keyboard can provide a
temporary input method, though it reduces portability. (Professor Messer, p. 1)

Individual keycaps and the mechanisms beneath them are delicate. Before lifting
or replacing a keycap, consult the manufacturer's instructions for that keyboard
design. Applying a generic removal method can damage parts that are more
difficult to replace than the cap itself. (Professor Messer, p. 1)

## Memory

Replaceable laptop memory commonly uses the Small Outline Dual In-line Memory
Module (SO-DIMM) form factor. A removable SO-DIMM provides a modular upgrade
path when the laptop has a compatible slot. (Professor Messer, p. 1)

Not every laptop exposes removable memory. When RAM is soldered to the system
board, there is no separate module to exchange; correcting a memory hardware
failure may require replacing the system board. Always confirm the physical
design before promising an upgrade. (Professor Messer, p. 1)

## Storage

Laptop hard disk drives (HDDs) store data on rotating magnetic media and commonly
use a compact 2.5-inch form factor. Solid-state drives (SSDs) store data without
moving parts, providing quiet operation and lower access latency. Some laptop
SSDs also use a 2.5-inch drive form factor. (Professor Messer, p. 1)

M.2 storage uses a smaller board-style form factor that installs directly into
a socket without separate drive data and power cables in the source's laptop
storage example. This physical description does not assign every M.2 drive to
one storage protocol. Physical access can still vary: a drive may sit behind a
service panel or require opening most of the laptop. (Professor Messer, p. 1)

## Storage Migration

Moving from an HDD to an SSD requires a plan for the operating system,
applications, settings, and user data. Two broad approaches are useful:

- **Clean installation:** Install the operating system and applications on the
  SSD, then move needed user data. This produces a fresh environment but requires
  more setup work.
- **Imaging or cloning:** Use imaging software to copy the existing environment
  so the operating system and applications do not need to be installed again.

An image-file workflow saves the source drive into an intermediate image that
can later be applied to a destination. A drive-to-drive clone copies directly
from the old drive to the new one. In either case, compatible imaging software
is required. (Professor Messer, p. 1)

## Wireless Hardware

Laptop wireless connectivity commonly includes 802.11 Wi-Fi and Bluetooth.
Wi-Fi serves local-area networking, while Bluetooth connects nearby peripherals
over a personal area network. (Professor Messer, pp. 1–2)

Wi-Fi antenna leads are commonly routed around the display assembly, placing the
antennas high in the laptop. Systems may have multiple antenna leads, such as
main and auxiliary connections. (Professor Messer, p. 2)

## Wireless and Short-Range Features

Bluetooth is intended for short-range connections to nearby devices and
peripherals. Near-field communication (NFC) operates over a much shorter
distance—about four centimeters or less—and can support small data exchanges or
authentication interactions. These technologies solve different proximity and
connection needs. (Professor Messer, p. 2)

## Biometrics

Fingerprint readers and face-recognition hardware support biometric sign-in or
unlock. Biometrics represent “something you are.” The feature requires suitable
hardware and operating-system configuration; compatible hardware alone does not
guarantee that biometric sign-in is configured. (Professor Messer, p. 2)

## Microphone

A built-in laptop microphone is commonly positioned in the display assembly and
is convenient for everyday calls. When the use case demands better or more
specialized audio capture, an external microphone—such as an analog or USB
device—may be the more appropriate choice. (Professor Messer, p. 2)

## Decision Summary

- Verify the exact model and service procedure before disassembly.
- Distinguish removable components from parts soldered to the system board.
- Choose storage by the stated requirement, not by a vague claim that one type
  is always better.
- Choose clean installation or cloning based on whether the existing software
  environment must be preserved.
- Recognize that Wi-Fi antenna leads may be routed around the display assembly.
- Use Bluetooth, NFC, biometrics, and microphones according to the specific
  range, authentication, or input requirement in the scenario.

## References

- Professor Messer 220-1201 v1.70 pp. 1–2
- CompTIA A+ 220-1201 Exam Objectives v2.0, Objective 1.1
