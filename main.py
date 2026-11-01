#Given a Scapy packet, check it has an IP layer,
#  then print source, destination, TTL and protocol. 
# If no IP layer exists, print No IP layer.

from scapy.all import *

if packet.haslayer(IP):
    print('Source:', packet[IP].src)
    print('Destination:', packet[IP].dst)
    print('TTL:', packet[IP].ttl)
    print('Protocol:'. packet[IP].proto)

else:
    print('No IP layer.')