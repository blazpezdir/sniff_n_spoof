from scapy.all import *


def spoof_reply(pkt):
    a = IP()
    a.dst = pkt['IP'].src
    a.src = pkt['IP'].dst

    b = ICMP()
    b.type = 0

    p = a / b
    send(p)


pkt = sniff(filter='icmp and src net 10.0.2.0/24', prn=spoof_reply);
