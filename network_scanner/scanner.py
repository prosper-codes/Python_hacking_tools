import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]

    print("ip\t\t\tMAC Address\n----------------------------------------")
    clients_list = []
    for item in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def display_results(results_list):
    print("IP\t\t\tMAC Address \n")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


scanned_result = scan("192.168.204/24")
display_results(scanned_result)
