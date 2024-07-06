import socket
from common_ports import ports_and_services
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def get_open_ports(target, port_range, verbose=False):

    open_ports = list(filter(lambda x: x != None, [port if (s.connect_ex(
        (target, port)) == 0) else None for port in range(port_range[0], port_range[1]+1)]))
    
    return (open_ports)


get_open_ports("scanme.nmap.org", [20, 80])
