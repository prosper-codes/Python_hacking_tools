import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    print("ip\t\t\tMAC Address\n----------------------------------------")
    for item in answered_list:
        print(item[1].psrc + "\t\t" + item[1].hwsrc)


scan("192.168.204/24")
