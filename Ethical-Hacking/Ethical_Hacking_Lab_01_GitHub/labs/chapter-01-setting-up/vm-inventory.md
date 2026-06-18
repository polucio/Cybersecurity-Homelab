# VM Inventory – Chapter 1

## OPNsense Firewall

| Setting | Value |
|---|---|
| Platform | VirtualBox |
| Firewall OS | OPNsense 26.1.6 |
| Base OS | FreeBSD 64-bit |
| vCPU | 2 |
| RAM | 2 GB |
| Adapter 1 | Bridged Adapter |
| Adapter 2 | Internal Network: Internal LAN |
| WAN Interface | em0 |
| LAN Interface | em1 |
| LAN IP | 192.168.1.1/24 |

## Metasploitable 2

| Setting | Value |
|---|---|
| Purpose | Vulnerable Linux target |
| Disk | Existing Metasploitable VMDK |
| Network | Internal Network: Internal LAN |
| Confirmed IP | 192.168.1.121 |
| Default Username | msfadmin |
| Default Password | msfadmin |

## Kali Linux

| Setting | Value |
|---|---|
| Purpose | Attacker/testing VM |
| Source | Kali VirtualBox image |
| Network | Internal Network: Internal LAN |
| Confirmed IP | 192.168.1.188 |
| Default Username | kali |
| Default Password | kali |

## Ubuntu Desktop

| Setting | Value |
|---|---|
| Purpose | Desktop VM for later chapters |
| Install Media | Ubuntu Disc Image File / ISO |
| Network | Internal Network: Internal LAN |
| Active Directory | Not used |
| Partitioning | Erase disk and install Ubuntu, virtual disk only |
| Notes | Parked after install until later chapters |
