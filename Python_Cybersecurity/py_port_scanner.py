import socket

def port_scanner(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
        
target_ip = '10.104.220.56'
ports_to_scan = [80, 630, 9100]
port_scanner(target_ip, ports_to_scan)