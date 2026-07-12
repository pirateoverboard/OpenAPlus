# Objective 1.5: Microsoft Command-line Tools

Objective 1.5 asks you to choose the appropriate Microsoft command-line tool
for a scenario. The practical skill is not typing every possible switch from
memory; it is recognizing which command fits a navigation, network, disk, file,
information, or operating-system management task.

Some commands can change data or system behavior. Commands such as `format`,
`diskpart`, `chkdsk` repair options, and Group Policy update commands should be
used with the correct scope and with awareness of the system being changed.
(CompTIA Objective 1.5; Professor Messer, p. 9)

## Navigation and File Management

Use `dir` to list files and directories in the current location. Use `cd` or
`chdir` to change the working directory. `..` refers to the parent directory,
and Windows paths commonly use drive letters and backslashes, such as
`C:\Users`. (Professor Messer, p. 9)

Use `md` or `mkdir` to create a directory, and use `rd` or `rmdir` to remove a
directory. Use `robocopy` when the task calls for a more capable file-copy tool
than older copy utilities, especially for structured file-copy jobs between
folders or systems. (CompTIA Objective 1.5; Professor Messer, p. 9)

The objective also includes `[command name] /?`. Use that form when you need
syntax help for a specific command at the prompt. It is a quick way to confirm
switches before running a command that could affect files, disks, or policy.
(CompTIA Objective 1.5; Professor Messer, p. 9)

## Disk Management Commands

Use `chkdsk` to check a disk file system. `chkdsk /f` fixes logical file-system
errors, while `chkdsk /r` locates bad sectors and recovers readable
information; the `/r` option includes the `/f` behavior. If the target volume is
locked, Windows may schedule the operation during startup. (Professor Messer,
p. 9)

Use `format` to prepare a disk or partition for Windows use. Treat it as a
destructive command because formatting can remove access to existing data. Use
`diskpart` to start the DiskPart command interpreter for disk, partition, and
volume configuration; it also carries data-loss risk when used incorrectly.
(CompTIA Objective 1.5; Professor Messer, p. 9)

## Informational Commands

Use `hostname` to display the Windows device name, which is helpful when many
remote sessions or terminal tabs are open. Use `winver` to open the About
Windows dialog and confirm Windows version information during troubleshooting.
(CompTIA Objective 1.5; Professor Messer, p. 9)

Use `whoami` to identify the current user context. `whoami /all` shows fuller
identity details, including group and privilege information. (CompTIA
Objective 1.5; Professor Messer, p. 9)

## OS Management Commands

Use `gpupdate` to force a Group Policy update instead of waiting for normal
refresh timing or sign-in processing. Use `gpresult` to verify which policy
settings apply to a computer or user. `gpupdate` applies policy; `gpresult`
reports policy results. (CompTIA Objective 1.5; Professor Messer, p. 9)

Use `sfc /scannow` to run System File Checker against protected Windows system
files. It is the command-line tool to consider when Windows system-file
integrity is in question. (CompTIA Objective 1.5; Professor Messer, p. 9)

## Network Commands

Use `ipconfig` to view TCP/IP and network adapter information. Use
`ipconfig /all` when you need additional configuration details such as DNS and
DHCP server information. (CompTIA Objective 1.5; Professor Messer, p. 10)

Use `ping` to test basic reachability and round-trip time with ICMP. A failed
ping does not always prove the destination is down because firewalls and
networks may filter ICMP, but ping remains a useful first connectivity test.
(Professor Messer, p. 10)

Use `netstat` for network statistics and active connection information.
`netstat -a` shows active connections, while `netstat -n` avoids name
resolution and displays numeric addresses. Use `nslookup` to query DNS
information such as names and IP addresses. (CompTIA Objective 1.5; Professor
Messer, p. 10)

Use `net use` to map a Windows network share to a drive letter, and use
`net user` to view user account information or perform supported account
actions from the command line. Use `tracert` to show the route a packet takes
to a destination. Use `pathping` when you need a route map plus round-trip and
packet-loss measurements at each hop. (CompTIA Objective 1.5; Professor
Messer, p. 10)

## Decision Summary

- Use `dir` to list files and directories.
- Use `cd` or `chdir` to change directories.
- Use `md` or `mkdir` to create a directory.
- Use `rd` or `rmdir` to remove a directory.
- Use `[command] /?` for command-specific syntax help.
- Use `chkdsk /f` for logical file-system repair.
- Use `chkdsk /r` for bad-sector checking and readable-data recovery.
- Use `format` to prepare a disk or partition, with data-loss caution.
- Use `diskpart` for disk, partition, and volume configuration.
- Use `robocopy` for robust file-copy tasks.
- Use `hostname`, `winver`, `whoami`, and `net user` for system, user, and
  account information.
- Use `gpupdate` to apply Group Policy updates and `gpresult` to verify applied
  policy.
- Use `sfc /scannow` for protected system-file integrity checks.
- Use `ipconfig`, `ping`, `netstat`, `nslookup`, `net use`, `tracert`, and
  `pathping` for network configuration and connectivity troubleshooting.

## References

- CompTIA A+ 220-1202 Exam Objectives v4.0, Objective 1.5
- Professor Messer 220-1202 v1.40 pp. 9-10
