#!/usr/bin/env python

__author__ = "bt3"

import netaddr
import socket

subnet = '192.168.1.0/24'

for ip in netaddr.IPNetwork(subnet):
    s = socket.socket()
    print ip
    s.connect((ip, 25))
    # send email packets