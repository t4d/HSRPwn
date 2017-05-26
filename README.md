# HSRPwn

HSRPwn is a simple tool that allows to declare - and keep UP - your host as THE gateway in a Cisco's HSRP LAN environment where default HSRP password is in use.
This script use to elect the chosen host to become the new LAN's gateway.

This tool can be used, as a PoC, to:
 * MITM LANs hosts (the desired gateway can sniff all traffic passing through it) 
 * DDOS a particular hosts (all traffic can be routed to the targeted host)
 * Black holing LANs hosts 

Because you change all the topology of your routing configuration: 
  ### !!!Take care of where you execute this!!!

## Requirements

[Scapy](https://pypi.python.org/pypi/scapy)

## Usage

Edit 'Vars' part:
 * 'IF' interface connected to LAN which send packets
 * 'IPADDR' must indicate real host's IP address to elect as gateway
 * 'GW_IPADDR' the 'real' HSRP Gateway's IP address
 * 'GW_HWADDR' the 'real' HSRP Gateway's MAC address

You can now launch HSRPwn.py, as root:
```bash
  $ sudo ./HSRPwn.py
  ........
```

## References

[Wikipedia - Hot_Standby_Router_Protocol](https://en.wikipedia.org/wiki/Hot_Standby_Router_Protocol)

[Cisco - hot-standby-router-protocol-hsrp](http://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html)
