# Validation Notes – Chapter 2

## Host Discovery

Kali discovered the two important lab hosts:

```text
192.168.1.1      OPNsense / gateway
192.168.1.121    Metasploitable / victim
```

## IP Forwarding

Kali IP forwarding was enabled:

```bash
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
cat /proc/sys/net/ipv4/ip_forward
```

Output:

```text
1
```

## Manual ARP Spoofing

Two `arpspoof` sessions were run from Kali and showed repeated ARP replies, indicating that spoofed ARP replies were being sent continuously.

## urlsnarf Validation

`urlsnarf` was started with root privileges:

```bash
sudo urlsnarf -i eth0
```

Captured evidence:

```text
192.168.1.121 - - [20/Jun/2026:13:59:51 -0400] "GET http://192.168.1.1/ HTTP/1.0" - - "-" "Wget/1.10.2"
```

## tcpdump Validation

`tcpdump` was used to confirm traffic visibility:

```bash
sudo tcpdump -i eth0 host 192.168.1.121 and port 80
```

Captured evidence included:

```text
192.168.1.121.34993 > OPNsense.internal.http
HTTP: GET / HTTP/1.0
```

## Python Scapy Spoofer Validation

The Python Scapy ARP spoofer was run from Kali:

```bash
sudo python3 arp_spoofer.py
```

The script started successfully without warnings:

```text
[*] Starting ARP spoofing.
[*] Victim:  192.168.1.121
[*] Gateway: 192.168.1.1
[*] Press Ctrl+C to stop.
```

On Metasploitable, the ARP table showed the gateway IP mapped to Kali's MAC address:

```text
OPNsense.internal (192.168.1.1) at 08:00:27:8A:35:D2 [ether] on eth0
? (192.168.1.188) at 08:00:27:8A:35:D2 [ether] on eth0
```

This confirmed that the Python ARP spoofer successfully poisoned the victim's ARP table.

## ARP Detector Validation

The defensive ARP detection script successfully identified suspicious ARP behavior.

Example alert:

```text
[!] Possible ARP spoofing detected!
Time:        2026-06-20 14:14:43
IP address:  192.168.1.1
Old MAC:     08:00:27:8a:35:d2
New MAC:     08:00:27:a0:7f:ae
```

The detector also saw mappings flip back and forth, which demonstrated that the same IP address was being associated with different MAC addresses.

## MAC Flooding Validation

A limited MAC flooding test was run with `macof`:

```bash
sudo macof -i eth0 -n 50
```

`tcpdump` captured the generated Layer 2 traffic:

```text
492 packets captured
492 packets received by filter
0 packets dropped by kernel
```

## Result

Chapter 2 was completed successfully.

The lab validated:

- Manual ARP spoofing
- Traffic capture
- ARP table poisoning
- Python ARP spoofing with Scapy
- Python ARP spoof detection
- MAC flooding behavior
- Defensive lessons for Layer 2 attacks
