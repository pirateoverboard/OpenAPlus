# Objective 5.2 interview scenarios

Use these prompts for spoken troubleshooting practice. They are intentionally
longer than regular Anki cards and are not exported to TSV output.

## Clicking or grinding drive

Question:
A user reports that a drive is making clicking or grinding noises and files are
opening slowly. What would you do?

Answer pattern:
I would treat possible data loss as the priority. I would avoid unnecessary
write-heavy repair attempts, check whether the data is backed up, preserve
readable data if policy allows, and escalate if the data is important or the
drive appears to be failing. I would document the sound, performance symptom,
drive detection state, backup status, and any steps already taken.

Mistakes to avoid:
- Do not run aggressive repairs before protecting recoverable data.
- Do not treat noise from a mechanical drive like a routine software issue.
- Do not promise recovery.

## Boot device not found

Question:
A workstation reports that no boot device was found. How would you approach it?

Answer pattern:
I would first verify the exact error and whether the drive is detected in
firmware. If the drive is not detected, I would check cables, power, interface
settings, and a known-good connection if appropriate. If the drive is detected
but the OS does not boot, I would treat it as a different path involving boot
configuration, boot files, or OS state while still considering data risk.

Mistakes to avoid:
- Do not assume Windows is corrupted before confirming drive detection.
- Do not replace the drive before checking simple physical causes.
- Do not ignore removable boot media or boot order.

## RAID warning

Question:
A storage array is beeping and reports a RAID warning. What should you do?

Answer pattern:
I would check the RAID management console first and identify the affected array,
volume, and drive status. I would not pull drives by guesswork. Before any
replacement or rebuild work, I would confirm backup status and escalate with the
alert text, failed-disk identifier if known, volume affected, current array
state, and steps already taken.

Mistakes to avoid:
- Do not pull a drive before identifying it in the console.
- Do not treat RAID as a replacement for backups.
- Do not perform vendor-specific rebuild steps without policy or escalation.

## Storage health warning

Question:
Monitoring reports worsening storage health warnings. What is the support
response?

Answer pattern:
I would treat the warning as an opportunity to act before users lose access. I
would verify backups, review health trends or alerts, plan replacement or
escalation, and document the evidence. I would avoid memorizing obscure
attribute numbers as the main decision point; the practical decision is whether
the warning trend creates data risk.

Mistakes to avoid:
- Do not wait for a total failure if warnings are worsening.
- Do not rely on one vague alert without checking trend or status.
- Do not ignore backup verification.

## Missing drive

Question:
A user says a drive disappeared. How would you narrow it?

Answer pattern:
I would first identify the drive type: internal, external, or mapped network
share. For an internal drive, I would check firmware detection and data/power
connections. For an external drive, I would check power, cable, port, and
adapter path. For a network share, I would check network availability and
reconnect behavior instead of treating it as local disk failure.
