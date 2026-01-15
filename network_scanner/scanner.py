#!/usr/bin/env python3

import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description="Simple ARP-based network scanner")

    parser.add_argument(
        "-t",
        "--target",
        dest="target",
        required=True,
        help="Target IP or IP range (e.g. 10.0.2.1/24)",
    )

    args = parser.parse_args()
    return args.target


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for sent, received in answered_list:
        clients_list.append({"ip": received.psrc, "mac": received.hwsrc})

    return clients_list


def display_results(results_list):
    print("IP\t\t\tMAC Address")
    print("----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


target_ip = get_arguments()
scan_result = scan(target_ip)
display_results(scan_result)
