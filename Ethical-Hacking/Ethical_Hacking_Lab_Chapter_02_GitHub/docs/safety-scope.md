# Safety and Scope

## Authorized Lab Scope

This repository documents a private home lab using local virtual machines.

Authorized lab targets:

- Metasploitable 2
- Ubuntu Desktop lab VM
- OPNsense firewall/router management from inside the lab
- Other intentionally created lab VMs

## Out of Scope

The following are not authorized unless separately documented and explicitly permitted:

- Public IP addresses
- Employer systems
- School systems
- Neighbor networks
- Cloud systems not owned or authorized
- Any system outside the VirtualBox lab network

## Isolation Rule

Metasploitable is intentionally vulnerable and must remain on:

```text
Internal Network: Internal LAN
```

It must not be attached directly to:

```text
Bridged Adapter
```

## Purpose

This lab is for ethical hacking education, defensive understanding, SecurityX/CASP+ study, and controlled experimentation.
