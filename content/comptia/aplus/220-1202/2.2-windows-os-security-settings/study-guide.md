# Objective 2.2: Windows OS Security Settings

Objective 2.2 asks you to choose and apply a basic Windows security setting for
a stated need. The central skill is selecting the control with the right scope:
malware protection, network traffic, account privilege, sign-in, permissions,
encryption, or centralized domain administration. (CompTIA Objective 2.2;
Professor Messer, pp. 28–30)

## Microsoft Defender Antivirus

**Microsoft Defender Antivirus** is the antivirus component built into Windows
and managed through the Windows Security app. Its real-time protection should
normally remain active. Temporarily disabling it can help isolate a suspected
compatibility problem, but doing so increases risk and should be limited to the
troubleshooting period.

Antivirus **definitions**, also called signatures, identify known threats.
Automatic updating is normally configured, and a technician can manually check
for protection updates when current definitions are needed. (Professor Messer,
p. 28)

## Windows Firewall

Windows Firewall filters network traffic. It should normally remain enabled,
although a technician may briefly disable it to test whether it is causing a
connection problem. Settings can differ among network profiles, such as Public
and Private.

Firewall rules should be as narrow as the requirement:

- A **port rule** allows or blocks traffic identified by a TCP or UDP port.
- An **application rule** permits or blocks traffic for a selected program.
- Blocking all incoming connections provides stricter protection and ignores
  ordinary inbound exceptions, which can be useful on an untrusted network.

Prefer a targeted rule to leaving the firewall disabled after testing.
(Professor Messer, p. 28; CompTIA Objective 2.2)

## Users, Groups, and Sign-In

A **local account** exists only on one Windows device. A **Microsoft account**
can connect the sign-in to Microsoft services and synchronize supported
settings between devices. A **domain account** is centrally managed through
Active Directory.

Privilege should match the task:

- A **standard user** performs routine work without broad rights to change the
  operating system.
- An **administrator** can perform privileged work such as installing a
  service or changing protected system settings.
- A **Guest** account provides very limited access for temporary or public use.
- The legacy **Power Users** group no longer provides the elevated middle tier
  it once did; on current Windows versions it is effectively comparable to a
  standard user.

Windows sign-in options include a username and password, a device-local PIN,
fingerprint or facial recognition, and Windows Hello or a security key for
passwordless authentication. **Single sign-on (SSO)** uses one authentication
event to provide access to permitted domain resources without a fresh prompt
for each one. Passwordless methods remove the password from that sign-in path;
they do not remove authorization policy or necessarily eliminate every other
factor or recovery method. (Professor Messer, p. 28)

## NTFS and Share Permissions

**NTFS permissions** apply when a file or folder is accessed locally or over
the network. **Share permissions** apply only when the resource is reached
through a network share. For network access, both layers can apply, and the
effective result is the most restrictive combination. An explicit deny takes
priority over an allow.

Permissions can be **explicit**, set directly on an object, or **inherited**
from its parent. Inheritance lets a parent folder's settings propagate to child
objects; explicit permissions take precedence over inherited permissions.

The official objective also names file and folder attributes. Windows object
properties should not be confused with authorization entries: access is
controlled by the applicable permissions. The approved notes do not define a
specific attribute list for Objective 2.2, so this draft does not require
memorizing one. (Professor Messer, p. 29; CompTIA Objective 2.2)

## Elevation and User Account Control

Even a member of the Administrators group does not use full administrative
rights for every process by default. **Run as administrator** starts a selected
application with elevated rights for a task that requires them.

**User Account Control (UAC)** creates a consent or credential boundary before
software receives elevated access. Its secure desktop helps prevent another
process from automatically interacting with the elevation prompt. Routine work
should remain at standard privilege, with elevation used only when the task
requires it. (Professor Messer, p. 29)

## BitLocker, BitLocker To Go, and EFS

Choose Windows encryption according to what must be protected:

- **BitLocker** encrypts an entire volume, including an operating-system
  volume, so data remains protected if the drive is removed and read elsewhere.
- **BitLocker To Go** applies volume encryption to removable storage such as a
  USB flash drive.
- **Encrypting File System (EFS)** encrypts selected files or folders on NTFS
  rather than the whole volume.

Encryption keys and recovery material matter. An EFS key tied to a user's
credentials can become inaccessible after an improper account reset, while a
lost BitLocker recovery method can prevent access to the encrypted volume.
(Professor Messer, p. 29)

## Active Directory Administration

**Active Directory (AD)** centrally stores and manages domain objects such as
users, computers, groups, and shared resources. A Windows device must join the
domain before it can participate in the domain's centralized authentication and
management.

Common domain administration tasks include:

- assigning a **log-in script** to automate user tasks at sign-in;
- arranging users and computers in **organizational units (OUs)** so
  administration and policy can follow the intended hierarchy;
- moving an object to another OU with Active Directory Users and Computers;
- assigning a network **home folder** for centrally managed user storage;
- applying **Group Policy** to users or computers for settings such as security
  requirements and log-in scripts;
- granting rights to a **security group** and managing access by changing group
  membership; and
- using **folder redirection** to place known folders such as Documents or
  Desktop on a network share.

Home folders provide an assigned network location, while folder redirection
changes where a known Windows folder stores its contents. Group-based access
and OU-based policy reduce repetitive per-user configuration. (Professor
Messer, pp. 29–30)

## References

- CompTIA A+ 220-1202 Exam Objectives v4.0, Objective 2.2
- Professor Messer 220-1202 v1.40 pp. 28–30
