# Cybersecurity Homelab

This repository documents my hands-on cybersecurity, networking, and SecurityX (CAS-005) learning environment.

The lab is built primarily in VirtualBox and is being used to reinforce cybersecurity concepts through controlled, isolated, and documented practice.

## Current Learning Path

### Ethical Hacking

This section follows *Ethical Hacking: A Hands-on Introduction to Breaking In* by Daniel G. Graham.

| Chapter | Lab Focus | Status |
|---|---|---|
| Chapter 01 | OPNsense firewall deployment, VirtualBox lab setup, Kali, Metasploitable, Ubuntu, and first exploit validation | Complete |
| Chapter 02 | ARP spoofing, on-path traffic capture, ARP table inspection, Python Scapy tools, ARP spoof detection, and MAC flooding | Complete |

## Current Focus

- SecurityX (CAS-005)
- Network Security
- OPNsense
- Kali Linux
- Metasploitable 2
- Virtualized Security Labs
- Layer 2 Attacks and Defenses
- Python for Security Tooling
- Defensive Validation and Documentation

## Lab Environment

| Component | Purpose |
|---|---|
| VirtualBox | Virtualization platform |
| OPNsense | Firewall/router and lab gateway |
| Kali Linux | Attacker/testing VM |
| Metasploitable 2 | Intentionally vulnerable target VM |
| Ubuntu Desktop | Additional lab VM for later exercises |

## Network Design

The lab uses an isolated internal VirtualBox network for vulnerable systems.

```text
Home Network / Internet
        |
   OPNsense WAN
        |
   OPNsense LAN
  192.168.1.1
        |
 VirtualBox Internal LAN
        |
 -------------------------------
 |              |              |
Kali      Metasploitable     Ubuntu
```

## Completed Labs

### Chapter 01 – OPNsense Firewall Deployment and First Exploit

Completed work included:

- Built the foundational VirtualBox lab environment
- Installed and configured OPNsense as the firewall/router
- Assigned WAN and LAN interfaces
- Imported Kali Linux
- Imported Metasploitable 2
- Installed Ubuntu Desktop
- Confirmed internal network connectivity
- Validated Kali discovery of Metasploitable
- Completed the first controlled exploit against Metasploitable's vulnerable vsFTPd service
- Confirmed root access and command execution inside the isolated lab

### Chapter 02 – ARP Spoofing and Layer 2 Attacks

Completed work included:

- Identified ARP spoofing as an on-path/man-in-the-middle attack
- Enabled IP forwarding on Kali
- Used `arpspoof` to position Kali between Metasploitable and OPNsense
- Captured HTTP traffic with `urlsnarf`
- Validated traffic visibility with `tcpdump`
- Inspected Metasploitable's ARP table to confirm poisoning
- Implemented a Python ARP spoofer with Scapy
- Implemented a Python ARP spoofing detector with Scapy
- Tested MAC flooding with `macof`
- Documented defensive takeaways and prevention concepts

## Repository Organization

```text
docs/
  safety-scope.md

labs/
  chapter-01-setting-up/
    README.md
    vm-inventory.md
    network-diagram.md
    validation-notes.md
    first-hack.md
    troubleshooting.md
    evidence/

  chapter-02-arp-spoofing/
    README.md
    attack-summary.md
    commands-used.md
    validation-notes.md
    arp-table-inspection.md
    python-scapy-notes.md
    mac-flooding.md
    troubleshooting.md
    defensive-takeaways.md
    code/
      arp_spoofer.py
      arpdetector.py
    evidence/
```

## Safety and Scope

This repository documents authorized local lab work only.

The intentionally vulnerable systems are kept inside an isolated VirtualBox internal network and are not exposed directly to the public internet or my home network.

Out of scope:

- Public IP addresses
- Employer systems
- School systems
- Neighbor networks
- Cloud systems not explicitly authorized
- Any system outside the local lab environment

## Notes

This project is focused on learning the full process, not just running tools:

- Build the lab
- Troubleshoot the environment
- Understand the attack
- Validate the result
- Document the evidence
- Identify defensive controls
