from scapy.all import IP, ICMP, TCP, send

packet = IP(dst="8.8.8.8")/ICMP()
print("--- Packet Summary ---")
send(packet)

packet = IP(dst="8.8.8.8")/TCP(dport=80, flags="S")
print("--- Packet Summary ---")
send(packet)