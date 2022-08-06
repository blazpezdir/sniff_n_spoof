from scapy.all import *

ipLayer = IP()
ipLayer.dst = '192.168.8.8'

icmpLayer = ICMP()

packet = ipLayer / icmpLayer

reply = sr1(packet, verbose=0, timeout=5)

if reply is None:
    # No reply =(
    print("No reply =(")
elif reply.type == 0:
    # We've reached our destination
    reply.show2()
else:
    # We're in the middle somewhere
    print("Error: ", reply.type)