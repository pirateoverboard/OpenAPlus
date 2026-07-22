# Objective 2.7: Workstation Security and Hardening

Objective 2.7 asks you to choose workstation protections for a stated risk.
Hardening reduces unnecessary exposure, limits what an account can do, and
protects stored information and unattended systems. The important skill is to
match the control to the problem rather than apply every control without a
reason. (CompTIA Objective 2.7; Professor Messer, p. 43)

## Protect Data at Rest

Data-at-rest encryption protects information stored on a workstation or
removable medium. Full-disk encryption covers a drive or volume, while
file-system encryption can protect selected files and folders. Encryption is
especially useful when a laptop or removable drive is lost or stolen because
possession of the storage device does not by itself reveal the stored data.

Encryption keys also require protection and recovery planning. Losing the only
usable recovery key can make legitimate recovery impossible, so an organization
should retain an authorized backup of that key. (Professor Messer, p. 43)

## Build a Deliberate Password Policy

Several password properties address different weaknesses:

- **Length** increases the amount an attacker must guess. A multiword
  passphrase can provide length while remaining memorable.
- **Character types and complexity** make simple or predictable choices less
  likely. A policy may require a mix of letters, numbers, or symbols, but a
  predictable pattern is still weak.
- **Uniqueness** prevents one exposed password from unlocking several accounts.
  Password history can also prevent immediate reuse.
- **Expiration** limits how long a password remains valid and prompts a change
  when the policy interval ends.

A password manager makes unique passwords practical by storing them in a
protected, encrypted database. The manager itself must be strongly protected
because it holds access to many accounts. (Professor Messer, p. 43)

## Protect Firmware Settings and Startup

BIOS/UEFI passwords add protection before the operating system starts. A
supervisor or administrator firmware password restricts changes to firmware
settings. A firmware user password can require authentication before the
computer boots. These controls serve different purposes from data-at-rest
encryption: preventing a normal boot does not encrypt a drive that is removed
and read elsewhere. (Professor Messer, p. 43)

## Use Safe End-User Practices

Configure a password-protected screensaver or screen lock to engage after a
reasonable period of inactivity, and lock the workstation manually when
stepping away. When work is finished—especially on a shared computer—log off so
the next person cannot continue under the previous user's session.

Protect portable hardware with measures such as a physical lock or secure
storage. Protect personally identifiable information (PII) and passwords from
casual observation by controlling where sensitive information is displayed,
positioning screens away from public sightlines, or using a privacy filter when
appropriate. (Professor Messer, p. 43)

## Manage Accounts Around Their Purpose

Apply least privilege: grant a user only the rights required for assigned work.
Group-based permissions can make consistent access easier to manage than many
individual exceptions.

Account controls can further narrow exposure:

- Restrict log-in times when access is legitimate only during defined hours.
- Disable the guest account and other accounts that are not required.
- Lock an account after a configured number of failed attempts to slow online
  password guessing.
- Use inactivity timeouts and screen locks to protect authenticated but
  unattended sessions.
- Give contractor or temporary accounts an expiration date so they stop
  working when the authorized period ends.

Account expiration disables an account at a chosen date; password expiration
requires a credential change. They solve different lifecycle problems.
(Professor Messer, p. 43)

## Remove Defaults and Unneeded Paths

Change the default administrator account name and password. Published or easily
guessed defaults give an attacker a known starting point.

Disable AutoRun so inserted media cannot automatically start a program through
its AutoRun instructions. Do not confuse this with AutoPlay, which presents
choices for handling media and can be configured separately.

Disable services that the workstation does not need. Every listening or
externally reachable service can add an attack path; removing an unused service
reduces that attack surface. Confirm that a service is unnecessary before
disabling it so required workstation functions are not broken. (Professor
Messer, p. 43)

## Scenario Selection Summary

- Stolen drive or laptop data: use data-at-rest encryption.
- Unauthorized firmware changes: use a supervisor/administrator BIOS/UEFI
  password.
- Unattended but active session: use a manual or timed screen lock.
- Finished shared session: log off.
- Excessive account authority: restrict permissions.
- Repeated online password guesses: use failed-attempt lockout.
- Temporary access that must end automatically: set account expiration.
- Unnecessary code or network entry points: disable AutoRun and unused
  services as applicable.

Choose the control that directly addresses the scenario, and avoid assuming
that one control—such as a login password—also encrypts data or removes every
other attack path. (CompTIA Objective 2.7; Professor Messer, p. 43)

## References

- CompTIA A+ 220-1202 Exam Objectives v4.0, Objective 2.7
- Professor Messer 220-1202 v1.40 p. 43
