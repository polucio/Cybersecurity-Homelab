# Ethical Hacking Home Lab

This repository documents a local cybersecurity lab built from *Ethical Hacking: A Hands-on Introduction to Breaking In* by Daniel G. Graham.

The original book lab uses pfSense as the firewall/router. This implementation uses OPNsense as a modern equivalent while preserving the same network design: one WAN-facing firewall adapter and one isolated internal lab LAN.

## Current Status

- VirtualBox installed
- OPNsense installed and assigned WAN/LAN interfaces
- Kali Linux imported from the VirtualBox image
- Metasploitable 2 imported using the existing VMDK disk
- Ubuntu Desktop installed for later lab chapters
- Kali successfully discovered OPNsense and Metasploitable on the internal LAN
- Metasploitable web service loaded from Kali

## Lab Safety

Metasploitable is intentionally vulnerable. It must remain isolated behind the firewall on the internal lab network.

Do not attach Metasploitable, Kali, or Ubuntu to Bridged Adapter unless a later lab explicitly requires a different design and the risk is understood.

## Repository Structure

```text
labs/
  chapter-01-setting-up/
    README.md
    vm-inventory.md
    network-diagram.md
    validation-notes.md
    troubleshooting.md
docs/
  safety-scope.md
```
