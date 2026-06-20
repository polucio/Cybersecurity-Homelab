# Inspecting ARP Tables

## Purpose

Inspect the victim's ARP table to confirm that ARP spoofing changed the local IP-to-MAC address mapping.

## Command

On Metasploitable:

```bash
arp -a
```

## Observed Output

During the Python Scapy ARP spoofing test, Metasploitable showed:

```text
OPNsense.internal (192.168.1.1) at 08:00:27:8A:35:D2 [ether] on eth0
? (192.168.1.188) at 08:00:27:8A:35:D2 [ether] on eth0
```

## Interpretation

Metasploitable believed:

```text
192.168.1.1 gateway = 08:00:27:8A:35:D2
192.168.1.188 Kali  = 08:00:27:8A:35:D2
```

This means the gateway IP was mapped to Kali's MAC address from the victim's perspective.

## Expected Normal State

Normally, the gateway IP should map to the real OPNsense MAC address:

```text
192.168.1.1 -> OPNsense MAC
```

## Poisoned State

During ARP spoofing, the victim saw:

```text
192.168.1.1 -> Kali MAC
```

## Result

The ARP table inspection confirmed that the ARP spoofing attack successfully poisoned the victim's ARP cache.
