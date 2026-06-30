# Objective 5.2 - Troubleshooting Storage Devices

Objective 5.2 focuses on storage and boot symptoms. A strong help desk answer
does not start by replacing the drive. It starts by protecting the user's data,
confirming whether the device is detected, checking simple physical causes, and
using diagnostics or logs to decide whether the issue is the drive, cabling,
power, firmware configuration, RAID array, or operating system.

## Storage failure symptoms

Read/write failures, long delays, constant drive activity, and loud clicking or
grinding are storage warning signs. Mechanical hard drives have moving parts, so
noise combined with poor performance or inaccessible data is a serious symptom.
If the drive still responds, preserve data before attempting risky repairs.

An SSD can fail differently from a hard drive. It may stop responding, become
read-only, or show data corruption without mechanical noise. The absence of
clicking does not prove storage is healthy.

## Boot failure symptoms

Boot errors should be separated into two questions: Is the storage device
recognized, and is the operating system bootable? A "boot device not found"
style error points first to drive detection, cabling, power, interface settings,
or boot order. An "operating system not found" style error can mean the drive is
present but the OS or boot files are not usable.

Start with noninvasive checks. Verify data and power cables, remove unintended
bootable USB media, confirm the boot sequence, and check whether the storage
interface is disabled in firmware. For a new installation, confirm the hardware
configuration and try another compatible storage interface or known-good system
when appropriate.

## Data loss and corruption

Data loss can be expensive or impossible to reverse. If a failing device is
still readable, the first priority is a current backup. Do not run repair steps
that may write heavily to the disk until the data-protection plan is clear. If
business-critical or irreplaceable data is involved, escalate before trying
recovery attempts that could make the damage worse.

## RAID symptoms and recovery

RAID failures are often reported by array alerts, error messages, audible alarms,
status lights, or console notifications. The safest first step is to check the
RAID management console and identify the affected array, volume, and disk. Do
not pull drives by guesswork; arrays differ, and the wrong action can turn a
recoverable failure into data loss.

RAID improves availability or performance depending on the level, but it is not
a substitute for backup. A technician should still confirm that backups exist
before replacement or rebuild work begins.

## S.M.A.R.T. and read/write performance

S.M.A.R.T. can report warning signs before a drive fully fails. A single metric
is less useful than a trend: increasing warning values, repeated notifications,
or alerts from NAS or monitoring software should trigger backup verification and
planned drive replacement.

Slow read/write performance should be measured rather than guessed. IOPS is a
broad measure of storage operations per second. It can help compare expected
storage behavior and distinguish a storage bottleneck from unrelated CPU,
memory, or application issues.

## Missing drives in the operating system

If the OS boots normally but another internal drive is missing, check firmware
detection first, then inspect data and power connections. For an external drive,
check its power and cable path before assuming the disk failed. For a missing
network share, verify reconnect-at-sign-in behavior, login scripts, and network
availability; a missing share is not the same as a failed local disk.

## Interview-ready troubleshooting language

- "I would first verify the exact boot error and whether the drive is detected
  before assuming the drive failed."
- "If the drive is making grinding or clicking noises, I would protect the
  user's data and avoid unnecessary writes before repair attempts."
- "For a missing boot device, I would check cables, power, boot order, removable
  media, and disabled storage interfaces before replacing hardware."
- "For a RAID alert, I would check the array console and identify the failed
  disk or volume instead of pulling drives by guesswork."
- "For S.M.A.R.T. warnings, I would verify backups and plan replacement before
  the drive becomes unavailable."
- "I would document symptoms, exact errors, drive detection status, diagnostics,
  backup status, and escalation details."

## References

- CompTIA 220-1201 Exam Objectives v2.0, Objective 5.2
- Professor Messer 220-1201 v1.70 p.50
- Professor Messer 220-1201 v1.70 p.51
