# Objective 1.2: OS Installations and Upgrades

Objective 1.2 focuses on choosing the right installation or upgrade method for
the situation. The official wording is scenario-based, so the important skill is
matching the requirement to a boot method, installation type, partition style,
drive format choice, or upgrade preparation step.

## Boot Methods

USB installation media is common when a technician needs local bootable media.
The USB device must be bootable, and the target computer must support USB
booting. Solid-state or hard drives can also store operating-system
installation files, while some external drives can mount ISO images and boot
through USB. (Professor Messer, p. 3)

PXE, or Preboot eXecution Environment, supports remote network installation
when the computer can boot from the network. Internet-based installation is
also possible in some environments, such as Linux distribution installers,
macOS recovery workflows, and Windows update workflows. (Professor Messer,
p. 3)

An internal hard drive can host a separate OS installation or a new bootable
partition. Multiboot systems present a boot menu so the user can choose between
two or more installed operating systems. This is useful when multiple OSs must
remain available on the same computer. (Professor Messer, p. 3)

## Installation Types

A clean install starts fresh. It wipes or replaces the existing operating
environment and requires planning for user data, applications, settings, and
drivers. It is useful when a device needs a fresh state or when the existing
configuration should not be preserved. (Professor Messer, pp. 3-4)

An in-place upgrade starts from inside the existing OS and keeps applications,
documents, and settings where supported. It is useful when the goal is to move
to a newer OS version while minimizing user disruption. Compatibility still has
to be checked before relying on this method. (Professor Messer, p. 4)

Image deployment installs a prepared clone or standardized image. It is
relatively quick and can be automated, making it useful for repeated system
builds. Remote network installation installs from a local server, shared drive,
or across the Internet. (Professor Messer, p. 3)

Zero-touch deployment automates the installation and configuration process. It
is designed to provide a streamlined user experience with company-specific
configuration and minimal manual setup after the user receives the device.
(Professor Messer, p. 3)

A recovery partition is a hidden partition that contains installation or
recovery files. A repair installation attempts to fix Windows OS problems
without modifying user files, but it is not the same as an OS version upgrade.
(Professor Messer, p. 3)

Third-party drivers may be needed during installation when the installer cannot
access required hardware such as a storage controller. In that case, loading
the correct driver can allow the installer to see the target disk or device.
(Professor Messer, p. 3)

## Partitioning

Partitioning divides a physical drive into logical areas. It can separate data,
support multiple operating systems, or prepare a drive for installation. A
formatted partition is called a volume in Microsoft terminology. Partitioning
and formatting can destroy data, so existing data and partition layout must be
reviewed before changes are made. (Professor Messer, pp. 3-4)

GPT, or GUID Partition Table, is the newer partition style. It requires UEFI
support and allows far more partitions and much larger partition sizes than MBR.
MBR, or Master Boot Record, is older and limited to 2 TB partitions and four
primary partitions. One MBR primary partition can be marked active, and an
extended partition can hold logical partitions. (Professor Messer, pp. 3-4)

## Drive Format

During installation, a quick format creates a new file table and makes the drive
appear empty, but it does not overwrite all previous data or perform extra disk
checks. A full format writes zeros across the disk and checks for bad sectors,
but it takes longer and makes the old data unrecoverable. (Professor Messer,
p. 4)

## Upgrade Preparation

Before an upgrade or installation, verify minimum and recommended OS
requirements, review the existing drive layout, and back up old data and user
preferences. Installation questions such as partition layout and license keys
should be planned before starting. (Professor Messer, p. 4)

Application and driver compatibility should be checked with the application
developer or hardware manufacturer. A hardware compatibility check can identify
problems before the upgrade starts. (Professor Messer, p. 4)

Windows lifecycle planning matters because quality updates, feature updates,
and support windows affect whether an OS version remains a good target. Feature
updates add new features, while quality updates focus on security fixes and bug
fixes. (Professor Messer, p. 4)

## Decision Summary

- Use USB boot media for local installation when the device supports USB boot.
- Use PXE or remote network installation when systems should boot and install
  from a network source.
- Use clean install for a fresh state; use in-place upgrade when preserving
  applications, documents, and settings is the priority and compatibility
  allows it.
- Use image deployment or zero-touch deployment for standardized or automated
  rollouts.
- Use repair installation to fix a damaged Windows installation, not to perform
  an OS version upgrade.
- Choose GPT for modern UEFI systems that need more partitions or larger
  partitions; recognize MBR's older 2 TB and primary-partition limits.
- Back up data and check hardware, application, and driver compatibility before
  installation or upgrade work.

## References

- CompTIA A+ 220-1202 Exam Objectives v4.0, Objective 1.2
- Professor Messer 220-1202 v1.40 pp. 3-4
