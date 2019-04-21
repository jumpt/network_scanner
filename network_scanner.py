#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()
    # in the lecture he keeps referring to these as packets??? and broadcast/arp_request is combining the packets??
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    # this creates the appropriate (E.G. DEST of pdst) field when we create the object
    # print(arp_request.summary())
    # print (broadcast.summary())
    # scapy.ls(scapy.Ether())
    # lists out all fields for scapy.etheR
    arp_request_broadcast = broadcast/arp_request



    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()
    # this shows more details about the packet



scan("10.0.3.0/24")

# test1

