# Objective 1.9: Linux Features and Tools

Objective 1.9 asks you to identify common Linux client and desktop features and
tools. The central skill is associating each command, configuration file, or OS
component with its purpose. Exact command options vary, so this guide emphasizes
the stable base commands named by the official objective. (CompTIA Objective
1.9; Professor Messer, pp. 18-21)

## File and Directory Management

- `ls` lists the contents of a directory.
- `pwd` prints the path of the current working directory.
- `mv` moves an item or renames it when the destination is a new name.
- `cp` copies files or directories.
- `rm` removes files or directories.
- `grep` searches text for a pattern.
- `find` searches directory trees for files that match criteria such as a name
  or extension.

Linux permissions and ownership are separate controls. `chmod` changes access
modes such as read, write, and execute for the owner, group, or others.
`chown` changes a file's owner and, when specified, its group. (Professor
Messer, pp. 19-20)

## Filesystems and Storage

`mount` associates a storage device or filesystem with a directory so its
contents are accessible through that mount point. `fsck` checks a filesystem
for logical errors and can repair supported problems; the approved notes call
for using it on an unmounted or read-only volume. (Professor Messer, p. 20)

For capacity information, `df` reports free space by filesystem, while `du`
reports space consumed by a file or directory. The `-h` option produces
human-readable size units for both tools. (Professor Messer, p. 21)

## Administrative Access

The root account has user ID 0 and full control of the system. `sudo` runs a
specified command with superuser or another user's authority, so the elevation
applies to that command. `su` changes the current shell to another user and
remains in that identity until the session is exited. (Professor Messer,
pp. 18, 20)

## Package Management

`apt` and `dnf` manage software packages. Both can install, update, and remove
software, but a distribution commonly uses one package-management family.
`dnf` manages RPM packages and replaced `yum` in its package-manager line.
Choose the tool supplied by the installed distribution rather than assuming
every Linux system provides both. (Professor Messer, p. 20)

## Network Tools

- `ip` displays and configures network interfaces, addresses, and routes.
- `ping` tests IP reachability and measures round-trip time with ICMP.
- `curl` retrieves data identified by a URL.
- `dig` queries DNS information.
- `traceroute` maps the network path toward a destination, although some
  devices may not return the ICMP responses it relies upon.

## Information and Editing

`man` opens the system reference manual for a command. `cat` displays or
concatenates file contents. `ps` shows process information and process IDs,
while `top` provides a continuously updated view of processes and resource
utilization. `nano` is a full-screen text editor commonly available on Linux.
(Professor Messer, p. 21)

## Common Configuration Files

- `/etc/passwd` records registered user accounts and account attributes.
- `/etc/shadow` stores password hashes and password-aging information.
- `/etc/hosts` provides local hostname-to-address mappings that can supplement
  or override DNS results.
- `/etc/resolv.conf` contains DNS resolver configuration.
- `/etc/fstab` lists filesystem mount definitions used to make storage
  available through the directory tree, including mounts processed at startup.

## Linux OS Components

The bootloader begins the operating-system startup process after firmware
selects a boot device. It loads the Linux kernel. The kernel is the protected
core of the OS: it manages processes and mediates interaction with hardware.
After the kernel starts `systemd`, `systemd` manages services and launches or
coordinates the remaining system processes. (Professor Messer, p. 18)

## Decision Summary

- Use `chmod` for permissions and `chown` for ownership.
- Use `sudo` for one elevated command and `su` when changing the shell's user
  identity.
- Use `df` for free filesystem space and `du` for the space used by a specific
  file or directory.
- Use `ps` for a process listing and `top` for a live resource view.
- Use `dig` for DNS data, `ping` for reachability, and `traceroute` for path
  discovery.
- Distinguish local name mappings in `/etc/hosts` from resolver settings in
  `/etc/resolv.conf`.
- Remember the startup relationship: bootloader, kernel, then `systemd`.

## References

- CompTIA A+ 220-1202 Exam Objectives v4.0, Objective 1.9
- Professor Messer 220-1202 v1.40 pp. 18-21
