from scapy.all import *
from scapy.all import IP, TCP

print("==================Capture network packets========================")
# Use Scapy to capture network packets
packets = sniff(count=10)
packets.summary()

print("================== Apply a filter to capture specific types of packets ========================")
# Apply a filter to capture specific types of packets
packets = sniff(filter="tcp", count=10)
packets.summary()

print("==================Capture 1 packet========================")
packet = sniff(count=1)[0]

print("==================Print the entire packet========================")
print(packet)

print("==================Print specific field========================")
print(packet.show())

print("==================Access layers========================")
if packet.haslayer(IP):
    print(" Source IP address...")
    print(packet[IP].src)
    print(" Source IP address...")
    print(packet[IP].dst)
  
if packet.haslayer(TCP):
    print(" Source IP address...")
    print(packet[TCP].sport)
    print(" Source IP address...")
    print(packet[TCP].dport)