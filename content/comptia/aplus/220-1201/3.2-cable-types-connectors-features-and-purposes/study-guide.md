# Objective 3.2: Cable Types, Connectors, Features, and Purposes

Objective 3.2 covers the basic cables and connector families a technician is
expected to recognize and choose from. The useful skill is matching the cable or
connector to the job: network runs, peripherals, video, storage cabling,
adapters, and common connector identification.

## Network cables

**Twisted-pair copper** is the familiar Ethernet cabling used for most office
network drops. Cable categories describe manufacturing and performance
requirements, so the category must meet the Ethernet standard being deployed.
Terminations normally use the T568A or T568B wiring standard, and the same
standard should be used consistently on both ends of a straight-through cable.

**UTP** has no extra shielding and is common for general twisted-pair Ethernet.
**STP** adds shielding to reduce interference and must be grounded properly.
Direct-burial cable is designed for outdoor underground runs and is commonly
shielded and weather resistant.

**Plenum-rated cable** is used where building code requires a jacket suitable
for air-handling spaces. The exam point is the jacket and installation
environment, not memorizing every jacket material.

**Coaxial cable** has a center conductor and outer shield around the same axis.
In A+ scenarios it is commonly associated with cable television, cable modems,
and F-type threaded connectors.

**Optical fiber** carries data with light instead of electrical signaling.
Single-mode fiber is used for longer-distance links and typically uses a laser
light source. Multimode fiber is used for shorter-distance links and can use a
less expensive light source.

## Peripheral cables

**USB** is used for peripherals such as keyboards, mice, printers, and external
storage. USB 2.0 and USB 3.0 are generations of the USB signaling standard.
USB-C is a connector shape, not a guarantee of one specific signal or speed.

**Thunderbolt** is a high-speed peripheral connection that can carry data and
power, and newer Thunderbolt versions use a USB-C connector. This is a common
exam trap: a USB-C-shaped port may carry USB, Thunderbolt, DisplayPort video, or
power depending on the device support.

**Serial** cabling remains useful for console or management access on some
devices. DB9 is the classic RS-232 connector, though modern systems may need a
USB-to-serial adapter.

## Video cables

**HDMI** is a digital audio/video connection common on televisions, monitors,
and projectors. **DisplayPort** is also digital and is common on PCs and
monitors; it can often adapt to HDMI or DVI when the device supports the needed
mode.

**DVI** is a video connector family that can carry digital, analog, or both
depending on the DVI variant. **VGA** is analog video only and does not carry
audio. **USB-C** can carry video on some systems, but only when the port and
cable support the required alternate mode.

## Hard drive cables

**SATA** uses separate data and power connections for internal drives. **eSATA**
is the external form of SATA for external storage connections. The connectors
are physically different even though both relate to SATA signaling.

## Adapters and converters

An **adapter** changes the physical connector when the signals are already
compatible. A **converter** changes the signal format when the source and
destination are not electrically compatible. For example, digital-to-analog
video usually needs conversion rather than a simple passive adapter.

## Connector recognition

**RJ45** is the common Ethernet modular connector. **RJ11** is smaller and is
associated with telephone or DSL connections. **F-type** is the threaded coaxial
connector used with cable TV and cable modem service.

Fiber connectors include **ST**, which twists to lock, **SC**, which pushes on
and pulls off, and **LC**, which is smaller and uses a clip. A **punchdown
block** terminates individual wires in structured cabling.

Common peripheral and power connectors include MicroUSB, MiniUSB, USB-C, Molex,
Lightning, and DB9. For flashcards, OpenAPlus focuses on durable recognition and
purpose, not every connector revision or vendor-specific cable marking.

## Intentionally limited detail

OpenAPlus does not card every exact pin color, every USB speed and cable-length
combination, every Thunderbolt revision detail, every video-mode bandwidth
table, every DVI pin variant, or every possible adapter pairing. Those details
are either volatile, too implementation-specific, or better checked against
device documentation during real support work.

## References

- CompTIA 220-1201 Exam Objectives v4.0, Objective 3.2
- Professor Messer 220-1201 v1.70 p.22
- Professor Messer 220-1201 v1.70 p.23
- Professor Messer 220-1201 v1.70 p.24
- Professor Messer 220-1201 v1.70 p.25
- Professor Messer 220-1201 v1.70 p.26
- Professor Messer 220-1201 v1.70 p.27
- Professor Messer 220-1201 v1.70 p.28
- Professor Messer 220-1201 v1.70 p.29
