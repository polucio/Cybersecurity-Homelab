# Ethical Hacking Home Lab

This repository documents a local cybersecurity lab built while working through *Ethical Hacking: A Hands-on Introduction to Breaking In* by Daniel G. Graham.

The lab is built in VirtualBox using OPNsense as the firewall/router, Kali Linux as the attacker/testing machine, Metasploitable 2 as the intentionally vulnerable target, and Ubuntu Desktop for later labs.

## Current Lab Progress

| Chapter | Lab | Status |
|---|---|---|
| Chapter 1 | Lab setup and first exploit | Complete |
| Chapter 2 | ARP spoofing, traffic capture, ARP detection, and MAC flooding | Complete |

## Current Lab Network

| Device | Role | IP Address |
|---|---|---:|
| OPNsense | Gateway / firewall / router | 192.168.1.1 |
| Kali Linux | Attacker / on-path machine | 192.168.1.188 |
| Metasploitable 2 | Victim / vulnerable target | 192.168.1.121 |
| Ubuntu Desktop | Later lab VM | 192.168.1.165 |

## Chapter 2 Summary

Chapter 2 focused on Layer 2 attacks and traffic visibility.

Completed work included:

- ARP spoofing with `arpspoof`
- IP forwarding on Kali
- HTTP traffic capture with `urlsnarf`
- Packet validation with `tcpdump`
- Inspecting ARP tables on Metasploitable
- Implementing an ARP spoofer in Python with Scapy
- Implementing an ARP spoofing detector in Python with Scapy
- MAC flooding with `macof`
- Defensive takeaways for preventing or reducing these attacks

## Repository Structure

```text
docs/
  safety-scope.md
labs/
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
      README.md
```

## Safety Notice

This lab is for authorized local cybersecurity practice only.

Metasploitable is intentionally vulnerable and must remain isolated on the VirtualBox internal lab network. Do not run these techniques against systems you do not own or do not have explicit permission to test.
