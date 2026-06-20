# Evidence Notes – Chapter 2

This folder is reserved for sanitized screenshots or notes from the Chapter 2 lab.

Suggested evidence:

- Kali showing IP forwarding set to `1`
- Two Kali terminals running `arpspoof`
- Kali running `sudo urlsnarf -i eth0`
- Kali `tcpdump` showing `HTTP: GET / HTTP/1.0`
- Metasploitable generating HTTP traffic with `wget http://192.168.1.1`
- Metasploitable `arp -a` showing the gateway IP mapped to Kali's MAC
- Python `arp_spoofer.py` running
- Python `arpdetector.py` showing a possible ARP spoofing alert
- `macof` output and `tcpdump` capture summary

Do not upload:

- Packet captures containing sensitive traffic
- Private keys
- Credentials
- Screenshots containing personal information
- VM disk files
- ISO files
