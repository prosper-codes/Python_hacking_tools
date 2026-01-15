# Network Scanner

A simple Python-based network scanner that discovers live hosts on a local network using ARP requests.

## Requirements

- Python 3
- Scapy
- Root / Administrator privileges

## Installation

Install Scapy if not already installed:

pip install scapy

## Usage

Run the script with a target IP or subnet using the -t or --target argument:

sudo python3 network_scanner.py --target 10.0.2.1/24

OR

sudo python3 network_scanner.py -t 10.0.2.1/24

## Example Output

## IP MAC Address

10.0.2.2 08:00:27:aa:bb:cc
10.0.2.3 08:00:27:dd:ee:ff

## Notes

- The scanner uses ARP, so it only works on the local network.
- The program must be run with elevated privileges.
- NAT-based virtual machines may not return results; use Bridged networking.

## Author

Student Network Security Assignment
