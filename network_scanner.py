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

    # answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)

    # srp is the function that will send the packet and will return two sets of values, which is why we have
    # two variables. We are just giving the packet to the function and it just sends it, it doesn't do anything
    # to the packet.

    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # this is a slightly different version of the line above, because we are only interested in the answered list we
    # get the srp method to only provide element 0, the answered list, by using [0]. Verbose=false means we can start
    # to tidy up the screen output

    # print(answered_list.summary())
    # this prints the summary of the answered variable (this particular variable is a list), .summary is a method
    # implemented by scapy. This line gets commented out because we want to parse the list and extract the useful
    # information not just use the built in method summary.

    print("IP\t\t\tMac Address\n-----------------------------------------")
    # the \t means insert a tab, \n means new line

    for element in answered_list:
        # print(element[1].psrc)
        # this will show the sending IP address
        # print(element[1].hwsrc)
        # this will show the sending mac address
        # print(element[1].show())
        # each element is made up of two sub elements, the packet sent[0] and the packet received[0], we're only
        # interested in the packet received so we want sub element 1. The show command will show the fields available
        # in the packet.

        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        # this combines the above print statements

    # print(arp_request_broadcast.summary())
    # the class has a summary method which displays a summary
    # arp_request_broadcast.show()
    # this shows more details about the packet

scan("10.0.3.0/24")

# test1

