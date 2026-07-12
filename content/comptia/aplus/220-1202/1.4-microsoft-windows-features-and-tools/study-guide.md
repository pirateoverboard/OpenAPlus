# Objective 1.4: Microsoft Windows Features and Tools

Objective 1.4 asks you to use Microsoft Windows operating system features and
tools in a scenario. The practical skill is selecting the right built-in tool
for the job: live performance review, historical logs, storage changes,
scheduled automation, driver management, certificates, local accounts, policy,
system inventory, cleanup, boot configuration, or registry editing.

## Task Manager

Task Manager gives a quick, real-time view of what the local system is doing.
It is the first built-in tool to consider when a user reports that a computer
is slow right now and you need to see CPU, memory, disk, network, or similar
activity. It can be opened from the secure attention screen, the taskbar
context menu, or with `Ctrl+Shift+Esc`. (CompTIA Objective 1.4; Professor
Messer, p. 7)

The Services tab provides quick start, stop, and restart actions for background
services. The Startup tab helps control which applications launch when a user
signs in. The Processes tab lists running applications, background processes,
and services so the technician can sort by resource usage. The Performance tab
shows live and historical resource views, while the Users tab shows connected
users and gives options such as disconnecting a user. (Professor Messer, p. 7)

## Microsoft Management Console Snap-ins

The Microsoft Management Console, `mmc.exe`, is a framework for loading
administrative snap-ins. The exam objective lists several snap-ins directly, so
focus on matching each snap-in to its support task rather than memorizing the
console framework by itself. (CompTIA Objective 1.4; Professor Messer, p. 8)

Event Viewer, `eventvwr.msc`, consolidates Windows logs. Use it when you need
to investigate what happened earlier, such as application errors, security
audits, setup messages, system warnings, or critical events. It is not the best
tool for a live resource spike; Task Manager or Resource Monitor is better for
that. (Professor Messer, p. 8)

Disk Management, `diskmgmt.msc`, manages local disk operations such as viewing
storage layout and working with volumes. Because disk operations can destroy
data, verify backups and the intended disk before making changes. (Professor
Messer, p. 8)

Task Scheduler, `taskschd.msc`, runs applications or scripts on a schedule or
trigger. Use it when a recurring maintenance task needs to run automatically
without a technician starting it each time. (Professor Messer, p. 8)

Device Manager, `devmgmt.msc`, is the Windows tool for hardware devices and
drivers. Use it when the support task is to inspect device or driver status,
especially after hardware or driver compatibility changes. (CompTIA Objective
1.4; Professor Messer, p. 8)

Certificate Manager, `certmgr.msc`, is used to view and manage user and trusted
certificates. Local Users and Groups, `lusrmgr.msc`, manages local user
accounts and group membership. Performance Monitor, `perfmon.msc`, collects
longer-term performance statistics, supports alerts, and stores reports for
trend analysis. Group Policy Editor, `gpedit.msc`, manages local policy on a
standalone device; domain environments can use centralized Group Policy tools.
(CompTIA Objective 1.4; Professor Messer, p. 8)

## Additional Windows Tools

System Information, `msinfo32.exe`, summarizes hardware resources, components,
and software environment details. Use it when you need a broad inventory of
system configuration rather than a live performance graph or a historical log.
(Professor Messer, p. 9)

Resource Monitor, `resmon.exe`, gives a detailed real-time view separated into
Overview, CPU, Memory, Disk, and Network categories. Use it when Task Manager
shows pressure but you need a deeper breakdown of which process, file, disk, or
network activity is involved. (Professor Messer, p. 9)

System Configuration, `msconfig.exe`, centralizes boot, startup, and service
configuration options. It is useful for controlled startup troubleshooting, but
changes can alter how Windows boots or which services run. (Professor Messer,
p. 9)

Disk Cleanup, `cleanmgr.exe`, helps remove unused or unnecessary files to free
space. Disk Defragment, `dfrgui.exe`, is the graphical defragmentation tool for
traditional hard drives; defragmentation is not a normal SSD maintenance task.
(CompTIA Objective 1.4; Professor Messer, p. 9)

Registry Editor, `regedit.exe`, edits the Windows Registry, a central
hierarchical configuration database used by Windows, drivers, services,
applications, the user interface, and security account data. Registry changes
can break the system, so back up the registry or relevant keys before editing.
(Professor Messer, p. 9)

## Decision Summary

- Use Task Manager for quick live resource, startup, process, service, and user
  checks.
- Use Event Viewer for historical Windows logs and past application or system
  events.
- Use Disk Management for disk and volume layout, with backup awareness.
- Use Task Scheduler for recurring or triggered scripts and applications.
- Use Device Manager for hardware and driver status.
- Use Certificate Manager for user and trusted certificates.
- Use Local Users and Groups for local accounts and group membership.
- Use Performance Monitor for longer-term performance collection, alerts, and
  reports.
- Use Group Policy Editor for local policy settings.
- Use System Information for broad system inventory.
- Use Resource Monitor for detailed real-time resource breakdowns.
- Use System Configuration for boot, startup, and service troubleshooting.
- Use Disk Cleanup to free disk space from unneeded files.
- Use Disk Defragment for traditional hard-drive defragmentation, not routine
  SSD maintenance.
- Use Registry Editor only when registry-level configuration is required and
  backup precautions are in place.

## References

- CompTIA A+ 220-1202 Exam Objectives v4.0, Objective 1.4
- Professor Messer 220-1202 v1.40 pp. 7-9
