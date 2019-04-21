#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # this creates the arp packet, the object accepts the the IP argument as a variable to be used when creating
    # the packet, pdst is the field that accepts the IP argument.
    # arp_request.show()
    # this shows the contents of the arp packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # this creates the ether packet, dst is the broadcast MAC address
    # broadcast.show()
    # this shows the contents of the broadcast packet
    # print(arp_request.summary())
    # the scapy.ARP class has a summary method which displays a summary
    # print (broadcast.summary())
    # the scapy.Ether class has a summary method which displays a summary
    # scapy.ls(scapy.Ether())
    # lists out all fields available for scapy.etheR
    arp_request_broadcast = broadcast/arp_request
    # combines the ether and arp packets into a single packet

    # print(arp_request_broadcast.summary())
    # the class has a summary method which displays a summary
    arp_request_broadcast.show()
    # this shows more details about the packet

scan("10.0.3.0/24")

# test1

