import socket # Networking ke liye library

def port_scanner(target_ip):
    print(f"Scanning Target: {target_ip}")
    
    # Hum port 1 se 100 tak check karenge
    for port in range(1, 1000):
        # Socket object banana
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # 1 second ka wait karega
        
        # Port check karne ki koshish
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        
        s.close() # Connection band karna

# Chalaane ke liye apna IP ya 'google.com' try karein
target = input("Enter target website or IP: ")
port_scanner(target)