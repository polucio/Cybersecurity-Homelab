# Evidence Notes – Chapter 2

This folder is reserved for sanitized screenshots or notes from the ARP spoofing lab.

Suggested evidence:

- Kali showing IP forwarding set to `1`
- Two Kali terminals running `arpspoof`
- Kali running `sudo urlsnarf -i eth0`
- Metasploitable generating HTTP traffic with `wget http://192.168.1.1`
- Kali `tcpdump` showing `HTTP: GET / HTTP/1.0`

Do not upload:

- Packet captures containing sensitive traffic
- Private keys
- Credentials
- Screenshots containing personal information
- VM disk files
- ISO files
