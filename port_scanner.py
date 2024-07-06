import socket
from common_ports import ports_and_services
import re


def get_open_ports(target, port_range, verbose=False):

    s = None
    hostname, ipaddr, response = ("", "", "")
    open_ports = []

    try:
        ipaddr = socket.gethostbyname(target)
    except socket.gaierror:
        if re.match(r"^(\d){1,3}\.(\d){1,3}\.(\d){1,3}\.(\d){1,3}$", target):
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"
    
    hostname = socket.getfqdn(ipaddr)


    for port in range(port_range[0], port_range[1]+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if s.connect_ex((target, port)) == 0:
            open_ports.append(port)
        s.close()

    if verbose:
        response += str.format("Open ports for {}{}\n",
                               hostname, " ("+ipaddr+")" if ipaddr != hostname else "")
        response += "PORT     SERVICE\n"
        for index, port in enumerate(open_ports):
            response += str.format("{}      {}{}", port,
                                   ports_and_services.get(port, "None"), "\n" if index != len(open_ports) - 1 else "")

    return response if verbose else (open_ports)


print(get_open_ports("209.216.230.240", [440, 445], False))
