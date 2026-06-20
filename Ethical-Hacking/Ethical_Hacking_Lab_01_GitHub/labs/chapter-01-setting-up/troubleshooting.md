# Troubleshooting Notes – Chapter 1

## Issue: Metasploitable Booted into OPNsense

### Symptom

The VM named Metasploitable showed an OPNsense login screen.

### Cause

The Metasploitable VM had the OPNsense virtual disk attached.

### Fix

Removed the incorrect OPNsense disk from the Metasploitable VM storage settings and attached the correct Metasploitable VMDK.

Correct disk:

```text
Metasploitable.vmdk
```

## Issue: OPNsense Booted from Installer

### Symptom

OPNsense showed:

```text
Root file system: /dev/iso9660/OPNSENSE_INSTALL
```

### Cause

The VM was still booting from the installer ISO.

### Fix

Installed OPNsense to the virtual disk, then removed the ISO from the virtual optical drive.

## Issue: OPNsense Had No Interfaces Assigned

### Symptom

OPNsense showed:

```text
No network interfaces are assigned.
```

### Fix

Used console option 1, Assign interfaces.

Assignments:

```text
WAN = em0
LAN = em1
```

VLANs were not used.

## Issue: OPNsense Interfaces Were Reversed

### Symptom

OPNsense showed LAN on the wrong interface, causing Kali to lose DHCP.

### Fix

Reassigned interfaces:

```text
WAN = em0
LAN = em1
```

Final correct state:

```text
LAN (em1) -> 192.168.1.1/24
WAN (em0) -> DHCP address
```

## Issue: Kali Had No IPv4 Address

### Symptom

Kali showed eth0 as up, but only had an IPv6 link-local address.

### Fix

Used NetworkManager:

```bash
nmcli device status
sudo nmcli device connect eth0
ip addr
```

## Issue: dhclient Not Installed on Kali

### Symptom

```text
sudo: dhclient: command not found
```

### Fix

Used NetworkManager instead:

```bash
sudo nmcli device connect eth0
```

## Issue: netdiscover Was Run on Metasploitable

### Symptom

```text
sudo: netdiscover: command not found
```

### Cause

`netdiscover` was run from Metasploitable instead of Kali.

### Fix

Run discovery tools from Kali:

```bash
sudo netdiscover -i eth0 -r 192.168.1.0/24
```

Use Metasploitable only to check its own IP if needed:

```bash
ifconfig eth0
```

## Issue: Ubuntu vmwgfx Warning

### Symptom

Ubuntu showed:

```text
vmwgfx is running on an unsupported hypervisor
```

### Notes

This is a graphics-driver warning. For the lab, it is usually safe to ignore if Ubuntu reaches the desktop.

Recommended VirtualBox display settings:

```text
Graphics Controller: VMSVGA
Video Memory: 128 MB
3D Acceleration: Disabled
```

## Issue: Ubuntu Asked About Active Directory

### Fix

Skipped Active Directory. This Ubuntu VM uses a normal local account.
