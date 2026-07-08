# Objective 3.3 study guide: RAM Characteristics

Objective 3.3 covers the RAM traits a technician should compare when choosing
or replacing memory: physical module form factor, DDR generation, ECC support,
and channel configuration. The exam skill is not memorizing every module speed
table. It is recognizing which characteristics must match the system and why.

## Scope and source handling

CompTIA 220-1201 Objective 3.3 defines the scope. Professor Messer 220-1201
v1.70 pages 30-31 were used as private validation/reference pages only. This
guide uses original wording and does not reproduce source tables, diagrams,
layout, or phrasing.

## RAM versus storage

RAM is working memory used by the CPU while software is running. It is separate
from long-term storage such as an SSD or hard drive. A program and its active
data must be in RAM before the CPU can work with them efficiently, but ordinary
RAM does not retain its contents after power is removed.

DRAM is dynamic memory, so it must be refreshed repeatedly to preserve data
while powered. SDRAM coordinates memory activity with the system clock. Modern
desktop and laptop memory is commonly described by DDR generation because DDR
memory transfers data on more than one part of a clock cycle.

## RAM form factors

**DIMM** stands for Dual In-line Memory Module. It is the larger memory module
form factor commonly used in desktop systems and many servers.

**SODIMM** stands for Small Outline Dual In-line Memory Module. It is a smaller
form factor commonly used in laptops and compact systems where physical space
is limited.

The form factor must match the system's memory slot. A desktop DIMM and a
laptop SODIMM are not interchangeable just because both are RAM.

## DDR iterations

DDR generations include DDR3, DDR4, and DDR5 in the approved source section.
Each newer generation improves memory capability, but DDR generations are not
drop-in interchangeable. The notch position, signaling, and motherboard support
must match.

For OpenAPlus cards, the durable exam point is compatibility by generation and
system documentation, not exact speed, capacity, or timing tables. A technician
should check the motherboard or system documentation before buying replacement
RAM.

## ECC and non-ECC RAM

ECC stands for Error-Correcting Code. ECC RAM can detect and correct certain
memory errors while the system is running. It is common in systems where memory
errors can be especially costly, such as servers and other critical systems.

Non-ECC RAM does not provide that same correction capability and is common in
consumer desktops and laptops. ECC support depends on the platform, so a
technician should verify system support before choosing ECC memory.

## Channel configurations

Memory channel configurations increase throughput between RAM and the CPU by
using more than one memory path. Dual-channel, triple-channel, and quad-channel
configurations depend on the memory controller and motherboard design.

For a channel configuration to work as intended, memory modules should be
installed in the correct slots and should be closely matched. Exact matches are
best because mismatched modules may prevent the platform from using the desired
channel mode or may force slower compatible settings.

## Intentionally limited details

OpenAPlus does not card exact DDR transfer rates, DIMM capacity limits, memory
timing strings, voltage details, motherboard slot color conventions, or every
server memory feature in this draft. Those details vary by platform or are more
usefully checked in system documentation. The cards focus on objective-scoped
selection and comparison concepts.

## References

- CompTIA 220-1201 Exam Objectives v4.0, Objective 3.3
- Professor Messer 220-1201 v1.70 p.30
- Professor Messer 220-1201 v1.70 p.31
