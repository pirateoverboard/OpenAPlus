# Objective 2.8: Mobile Device Security

Objective 2.8 asks you to choose a mobile-device security method for a stated
risk or management need. A useful answer matches the control to the goal:
protect stored data, prevent unauthorized use, keep software current, manage a
fleet consistently, respond to loss, or recover information. (CompTIA
Objective 2.8; Professor Messer, p. 44)

## Harden the Device

Full-device encryption protects data stored on a phone or tablet. The device
retains the encryption key, and access is tied to the device's authentication
controls. Encryption is especially important when a device is lost or stolen
because physical possession alone should not expose its stored information.

A screen lock restricts access to an unattended device. The official objective
includes facial recognition, PIN codes, fingerprints, patterns, and swipe as
screen-lock methods. Facial recognition and fingerprints use biometric traits;
the other listed choices use an on-screen interaction or secret. An
organization should select and configure the permitted methods through its
security requirements rather than assume every method offers the same
protection. (CompTIA Objective 2.8; Professor Messer, p. 44)

## Apply Configuration Profiles and MDM

A configuration profile is a predefined collection of device settings. It can
contain items such as corporate email details, lock-screen requirements,
passcode rules, or encryption requirements. Profiles let administrators apply
consistent settings to many devices or groups instead of configuring each
device manually.

Mobile device management (MDM) provides centralized administration for mobile
devices. An MDM platform can distribute configuration profiles and manage
controls for applications, data, cameras, authentication, and other device
features. Depending on policy and ownership, management may apply to the whole
device or to a managed work area. (Professor Messer, p. 44)

## Keep the OS and Applications Patched

Mobile patch management covers two distinct layers:

- **OS updates** provide operating-system security fixes, bug fixes, and
  platform changes.
- **Application updates** replace outdated app versions and address defects or
  security problems in those applications.

Updating only one layer can leave the other exposed. Devices should follow the
organization's approved update process and should not fall behind on either OS
or application updates. (CompTIA Objective 2.8; Professor Messer, p. 44)

## Use Endpoint Security Software

Antivirus and anti-malware software identify or block malicious software on the
endpoint. Availability and need can vary with the mobile platform, but the
objective-level decision is to use malware protection when the scenario calls
for detecting or preventing malicious code.

Content filtering serves a different purpose: it limits access to selected
websites or applications. It can enforce organizational access rules and reduce
exposure to unwanted content, but it is not a substitute for patching or
malware protection. (CompTIA Objective 2.8; Professor Messer, p. 44)

## Respond to Loss and Preserve Data

Several remote controls address different outcomes:

- A **locator application** uses available location services to help find a
  device. It may also make the device sound or display a message.
- A **remote wipe** deletes device data when recovery is unlikely or the risk
  of unauthorized disclosure is too high.
- A **remote backup application** copies data to a remote service so it can be
  restored to a replacement or recovered device.

These controls are complementary. Location helps recover hardware, wiping
protects data remaining on the device, and backup preserves a recoverable copy.
A backup does not erase the lost device, and a wipe does not create a backup.
(Professor Messer, p. 44)

Restrictions on failed log-in attempts reduce repeated guessing against the
screen lock. Depending on the configured policy, repeated failures can lock the
device, require additional account authentication, or trigger a wipe. The
threshold and response are policy choices rather than universal values.
(CompTIA Objective 2.8; Professor Messer, p. 44)

## Set Policies for Ownership and Profiles

Mobile policies must distinguish bring your own device (BYOD) from
corporate-owned devices. Ownership affects which devices enter management and
the scope of controls applied to them. The policy should state the applicable
profile security requirements, such as required screen locks, passcodes, or
encryption, and administrators can enforce supported requirements through MDM
and configuration profiles. (CompTIA Objective 2.8; Professor Messer, p. 44)

## Scenario Selection Summary

- Protect stored information on a lost device: full-device encryption.
- Apply the same settings to a device group: configuration profiles through
  MDM.
- Correct an outdated platform or app: install the corresponding OS or
  application update.
- Detect malicious code: antivirus or anti-malware software.
- Restrict selected sites or applications: content filtering.
- Find a misplaced device: a locator application.
- Remove information from an unrecoverable device: remote wipe.
- Restore information to a replacement device: remote backup.
- Slow repeated unlock guesses: failed log-in attempt restrictions.

Choose the control whose direct purpose matches the scenario instead of
treating encryption, location, wiping, and backup as interchangeable.

## References

- CompTIA A+ 220-1202 Exam Objectives v4.0, Objective 2.8
- Professor Messer 220-1202 v1.40 p. 44
