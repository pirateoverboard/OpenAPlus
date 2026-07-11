# Objective 3.5: Motherboards, CPUs, and Add-on Cards

Objective 3.5 covers the choices a technician makes when installing or
configuring the core platform hardware in a computer: motherboard form factor,
motherboard connectors, CPU compatibility and architecture, firmware settings,
expansion cards, and cooling.

## Motherboard Form Factors

The motherboard form factor affects case fit, expansion room, power connector
layout, and airflow planning.

ATX is the full-size desktop form factor in this objective. It is the best fit
when the system needs more expansion slots, more room around components, and a
standard desktop tower layout.

microATX is smaller than ATX and commonly fits many ATX-style cases, but it
usually provides fewer expansion slots. It is useful when a desktop needs a
smaller board without moving all the way to a very small system.

ITX is the small-form-factor choice. It is useful for compact, low-power, or
single-purpose systems where size matters more than expansion capacity.

## Motherboard Connectors

Expansion slots provide a path for add-on cards. PCI is an older parallel bus
found on previous generations of systems. PCIe is the modern serial expansion
standard and is commonly used for video cards, capture cards, NICs, and other
high-bandwidth adapters.

Power connectors provide power to the motherboard and high-power add-on cards.
A main ATX motherboard power connector is commonly 24-pin or 20+4-pin. Some
PCIe cards, especially video cards, require separate 6-pin or 8-pin PCIe power
connectors.

SATA connects internal storage devices. eSATA is the external form of SATA and
is used for external storage connections. Headers are small motherboard pin
blocks used for wiring connections. M.2 is a compact motherboard connector
commonly used for storage and some expansion devices.

## Motherboard Compatibility

CPU socket type is a hard compatibility boundary. The motherboard must support
the CPU vendor, socket, chipset/platform, and firmware requirements. AMD and
Intel processors are not interchangeable between socket families.

Multisocket motherboards support more than one physical CPU package. They are
associated with server-style workloads and are not the same thing as multicore
CPUs, where one CPU package contains multiple processing cores.

## BIOS and UEFI Settings

BIOS or UEFI firmware initializes hardware, performs startup checks, and starts
the boot process. UEFI is the modern firmware interface and supports modern
features such as Secure Boot.

Common firmware settings in this objective include boot options, USB
permissions, TPM security features, fan behavior, Secure Boot, boot passwords,
BIOS/supervisor passwords, temperature monitoring, and virtualization support.

Boot order controls which device the system tries first when starting. USB
permissions can allow or block USB devices for security. Temperature monitoring
and fan controls help verify cooling behavior without relying on the operating
system.

Secure Boot checks that trusted startup software is used during boot. A boot
password blocks system startup until the user enters the password. A
BIOS/supervisor password protects firmware setup changes. Lost firmware
passwords may require a motherboard reset procedure such as using a jumper,
depending on the system documentation.

Hardware virtualization support is enabled or disabled in firmware. It allows a
hypervisor to use processor virtualization features efficiently.

## TPM, HSM, and Encryption Support

A Trusted Platform Module (TPM) is tied to a single system. It provides
hardware-backed cryptographic functions and secure key storage for that local
device.

A hardware security module (HSM) is used by many systems or services. It is
often deployed as a dedicated appliance or high-end hardware device to protect
shared or centralized cryptographic keys.

The practical distinction is scope: TPM is local-device trust, while HSM is
centralized or multi-system key protection.

## CPU Architecture and Cores

x86 commonly refers to 32-bit PC architecture, while x64 refers to 64-bit PC
architecture. A 64-bit operating system and processor combination supports
larger memory addressing and 64-bit applications.

ARM is a reduced-instruction-set architecture commonly associated with efficient
processing, low power use, and lower heat output. This makes it common in
mobile, embedded, and some compact systems.

Core configuration describes how many processing cores are available inside a
CPU package. Dual-core, quad-core, octa-core, and multicore CPUs can process
more work in parallel than a single-core CPU, assuming the workload and
software can use the cores.

## Expansion Cards

Expansion cards add capabilities that are not present on the motherboard or
that need a higher-performance dedicated adapter.

Sound cards add audio output or input capabilities. Video cards provide
dedicated graphics processing and display outputs. Capture cards receive video
input from external sources for recording or streaming. Network interface cards
add or replace network connectivity.

Before installing an add-on card, check motherboard slot compatibility, case
clearance, power requirements, operating system support, and driver
requirements.

## Cooling

Cooling keeps the system within safe operating temperatures. Case fans move air
through the chassis. Heat sinks move heat away from components by conduction
and use fins to increase surface area. Thermal paste or thermal pads improve
contact between a hot component and a heat sink. Liquid cooling moves heat to a
radiator where fans can remove it from the system.

Cooling decisions should account for airflow path, cable routing, component
placement, fan size and noise, and the heat output of high-performance parts.
Avoid memorizing product-specific fan or temperature values; check system and
component documentation for exact requirements.

## References

- CompTIA 220-1201 Exam Objectives v4.0, Objective 3.5
- Professor Messer 220-1201 v1.70 pp.34-39
