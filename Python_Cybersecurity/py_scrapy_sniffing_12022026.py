from scapy.all import IP, ARP, sniff, wrpcap, rdpcap, getmacbyip

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        print(f"New Packet: {ip_layer.src} -> {ip_layer.dst}")
        
print("========== Start Sniffing ===========================")
sniff(filter="ip", prn=packet_callback, count=10)

# Use the wrpcap function to write packets to a file and rdpcap to read packets from a
# file.

print("Capture packets and save to a file")
packets = sniff(count=10)
wrpcap('packets.pcap', packets)

print("Read packets from the file")
saved_prackets = rdpcap('packets.pcap')
saved_prackets.summary()


print("Detect ARP Spoofing....")

def detect_arp_spoof(packet):
    if packet.haslayer(ARP):
        if packet[ARP].OP == 2:  # ARP response
            real_mac = getmacbyip(packet[ARP].psrc)
            response_mac = packet[ARP].hwsrc
            
            if real_mac !=  response_mac:
                print(f"ARP Spoofing Detected: {packet[ARP].psrc} is being claimed by {response_mac} instead of {real_mac}")
                
sniff(filter="arp", prn=detect_arp_spoof, store=0)