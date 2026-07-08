# Objective 3.4 study guide: Storage Devices

Objective 3.4 compares storage devices by how they retain data, connect to the
system, fit physically, and provide speed or redundancy. The exam focus is
choosing the right storage type or drive configuration for a requirement, not
memorizing every benchmark or vendor-specific feature.

## Scope and source handling

CompTIA 220-1201 Objective 3.4 defines the scope. Professor Messer 220-1201
v1.70 pages 32-34 were used as private validation/reference pages only. The
Professor Messer practice exams were used only as a private gap check for
official-scope storage and RAID concepts. This guide uses original wording and
does not reproduce source tables, diagrams, question wording, answer choices,
or explanations.

## Hard drives

Hard disk drives store data magnetically on spinning platters. They are
non-volatile, so they retain data when power is removed, but their moving parts
limit access speed and introduce mechanical failure risk.

Spindle speed is measured in revolutions per minute (RPM). A faster spindle can
reduce rotational delay, but real drive performance also depends on interface,
cache, workload, and drive design. For Objective 3.4, treat spindle speed as a
comparison characteristic, not as a promise of exact performance.

Common hard-drive form factors include 2.5-inch and 3.5-inch drives. The smaller
2.5-inch form factor is common in laptops and compact systems. The larger
3.5-inch form factor is common in desktop systems and many storage enclosures.

## Solid-state drives

Solid-state drives use non-volatile flash memory and have no spinning platters
or moving actuator arm. They are typically much faster at random access than
hard drives because they do not wait for mechanical movement.

An SSD still must match the system interface and physical form factor. A system
may support SATA SSDs, NVMe SSDs, PCIe add-in storage, M.2 drives, or older
mSATA drives depending on the motherboard and device design.

## Interfaces and form factors

SATA is a common storage interface originally designed around hard drives. SATA
SSDs are useful when a system has SATA drive bays or SATA cabling, but SATA can
limit the speed of modern SSDs compared with PCIe-based options.

NVMe is a storage protocol designed for SSD performance and commonly uses PCIe
as the transport. Many NVMe drives use an M.2 slot, but M.2 describes the
physical module interface and keying, not a guarantee of NVMe support. Always
check the system documentation for supported M.2 keys and whether the slot uses
NVMe, SATA/AHCI, or both.

PCIe storage connects through the PCI Express bus and can provide high
throughput for SSDs. PCIe storage may appear as an add-in card or as an M.2
drive using PCIe lanes.

SAS is Serial Attached SCSI. It is associated with higher-end storage systems
and storage arrays where management, throughput, and enterprise drive support
matter.

mSATA is Mini-serial Advanced Technology Attachment. It placed SATA storage
into a smaller card-like form factor used in some laptops and compact devices,
but it has largely been replaced by M.2 in modern systems.

## Removable and optical storage

Flash drives and memory cards are removable flash-based storage. They are useful
for portability and quick file transfer, but they are easy to lose or damage and
are not a substitute for a real backup plan.

Optical drives use removable discs such as CD, DVD, or Blu-ray media. They are
slower than modern solid-state storage but may still be used for legacy
installation media, offline distribution, or archival-style storage where the
environment and media quality are appropriate.

## RAID configurations

RAID combines multiple physical drives into a storage configuration for
performance, redundancy, or both. RAID is not a backup: it can improve
availability after some drive failures, but it does not protect against deleted
files, malware, corruption, theft, or disaster.

RAID 0 stripes data across drives for performance and capacity efficiency. It
does not provide redundancy. If one drive in a RAID 0 array fails, the array's
data is lost.

RAID 1 mirrors data across drives. It provides redundancy because each block is
duplicated, but usable capacity is reduced because the same data is stored on
more than one drive.

RAID 5 stripes data with parity and requires at least three drives. It provides
better usable capacity than mirroring while allowing the array to keep data
available after one drive failure.

RAID 6 adds a second parity set and requires at least four drives. It can keep
data available after two drive failures, but the extra parity consumes capacity
and adds overhead.

RAID 10, also written RAID 1+0, stripes across mirrored pairs. It combines the
performance benefit of striping with mirror-based redundancy and requires at
least four drives.

## Intentionally limited details

OpenAPlus does not card exact spindle-latency tables, every SSD benchmark,
every optical format capacity, every flash-memory electrical detail, or
vendor-specific M.2 keying tables in this draft. Those details vary by platform
or are better checked in system documentation. The cards focus on durable
selection, compatibility, redundancy, and performance concepts.

## References

- CompTIA 220-1201 Exam Objectives v4.0, Objective 3.4
- Professor Messer 220-1201 v1.70 p.32
- Professor Messer 220-1201 v1.70 p.33
- Professor Messer 220-1201 v1.70 p.34
