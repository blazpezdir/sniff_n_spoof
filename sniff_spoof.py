from scapy.all import *


def spoof_reply(pkt):
    a = IP()
    a.dst = pkt['IP'].src
    a.src = pkt['IP'].dst
    # We recognize a successful spoof in wireshark by looking if the ttl matches
    a.ttl = 111

    b = ICMP()
    b.type = 0

    p = a / b
    send(p)


pkt = sniff(filter='icmp and src net 10.0.2.0/24', prn=spoof_reply);
