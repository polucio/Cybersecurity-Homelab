#!/usr/bin/env python3

from scapy.all import ARP, sniff
from datetime import datetime

arp_table = {}


def process_packet(packet):
    if packet.haslayer(ARP):
        arp = packet[ARP]

        # ARP reply: "IP address X is at MAC address Y"
        if arp.op == 2:
            ip = arp.psrc
            mac = arp.hwsrc

            if ip not in arp_table:
                arp_table[ip] = mac
                print(f"[+] Learned {ip} is at {mac}")

            elif arp_table[ip] != mac:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("\n[!] Possible ARP spoofing detected!")
                print(f"    Time:        {timestamp}")
                print(f"    IP address:  {ip}")
                print(f"    Old MAC:     {arp_table[ip]}")
                print(f"    New MAC:     {mac}\n")

                # Update the table so the detector can continue tracking changes.
                arp_table[ip] = mac


print("[*] ARP detector started.")
print("[*] Listening for ARP replies. Press Ctrl+C to stop.\n")

sniff(filter="arp", prn=process_packet, store=False)
