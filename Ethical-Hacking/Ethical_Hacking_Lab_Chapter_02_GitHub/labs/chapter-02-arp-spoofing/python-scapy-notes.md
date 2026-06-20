# Python Scapy Notes – Chapter 2

## Scapy Verification

Scapy was already installed on Kali.

Verification command:

```bash
python3 -c "from scapy.all import *; print('Scapy works')"
```

Output:

```text
Scapy works
```

## Kali pip Note

Attempting to install Scapy with pip triggered Kali's externally managed environment warning.

The correct Kali-safe approach is to use the system package if Scapy is missing:

```bash
sudo apt update
sudo apt install python3-scapy
```

In this lab, Scapy was already present.

## Python ARP Spoofer

The Python ARP spoofer used Scapy to build Ethernet + ARP packets and send forged ARP replies.

Initial attempts using only `send()` with an ARP packet generated this Scapy warning:

```text
WARNING: You should be providing the Ethernet destination MAC address when sending an is-at ARP.
```

The corrected version used:

```python
Ether(dst=target_mac) / ARP(...)
sendp(packet, iface=interface, verbose=False)
```

This provided the Ethernet layer and removed the warning.

## Python ARP Detector

The ARP detector watched ARP replies and tracked IP-to-MAC mappings.

It alerted when the same IP address appeared with a different MAC address.

Example:

```text
[!] Possible ARP spoofing detected!
IP address:  192.168.1.1
Old MAC:     08:00:27:8a:35:d2
New MAC:     08:00:27:a0:7f:ae
```

## Learning Outcome

This section connected tool usage to implementation.

Instead of only running `arpspoof`, the lab recreated the basic ARP spoofing behavior in Python and then built a simple defensive detector to identify suspicious ARP changes.
