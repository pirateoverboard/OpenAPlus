# Objective 5.2 interview answer bank

These talk tracks support Objective 5.2 interview practice. Keep regular Anki
cards focused on one storage troubleshooting decision.

## What to say first

- "I would first verify the exact error and whether the storage device is
  detected before assuming it failed."
- "I would protect user data before attempting risky repair."
- "I would separate a missing drive from an unbootable operating system."

## Information to gather

- Exact boot, read/write, or storage-health error.
- Whether firmware detects the drive.
- Whether the OS sees the drive, external device, or mapped share.
- Any clicking, grinding, status lights, or repeated health alerts.
- Backup status and data criticality.
- Recent movement, installation, cabling, power, or firmware changes.

## Reasoning language

- "Drive detected but OS not found is different from drive not detected."
- "A noisy mechanical drive with slow access raises the data-risk level."
- "A RAID alert should be verified in the management console before physical
  action."
- "A missing mapped drive is a network or reconnect question before it is a
  local disk question."

## What to document

- Exact error or alert.
- Drive detection status.
- Cable, power, port, and firmware checks.
- Storage health or diagnostic results.
- Backup status and data-risk concerns.
- RAID array, volume, and failed-disk identifier if known.

## When to escalate

- Important data is at risk and recovery could become harder.
- Mechanical drive noise suggests possible failure.
- RAID state is degraded or unclear.
- The required repair is vendor-specific or outside help desk policy.
