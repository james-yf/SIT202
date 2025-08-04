import socket

# canonical name : IP address
A_records = {
    "pamelabeesly.com": "45.67.89.123",
    "jimhalpert.com": "102.154.76.88",
    "michaelscott.com": "172.32.210.5",
    # domain does not exist in CNAME_records
    "ryanhoward.com": "102.89.174.23"
}

# alias name : canonical name
CNAME_records = {
    "blog.pamelabeesly.com": "pamelabeesly.com",
    "www.pamelabeesly.com": "pamelabeesly.com",
    "blog.jimhalpert.com": "jimhalpert.com",
    "www.jimhalpert.com": "jimhalpert.com",
    "blog.michaelscott.com": "michaelscott.com",
    "www.michaelscott.com": "michaelscott.com",
    # fail case for lookup (does not exist in A_records)
    "www.dwightshcrute.com": "dwightshrute.com"
}

server_info = ('localhost', 11124)
query_buff = 100

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_info)

print("The server is running and awaiting a query from the client!")

while True:
    query, client_info = server_socket.recvfrom(query_buff)
    domain_name = query.decode()
    print(f"Server received the DNS query for [{domain_name}] from the client.\n")
    
    if domain_name == "terminate":
        print("The server program is terminating...")
        break

    elif domain_name in A_records:
        domain_IP = A_records[domain_name]
        server_socket.sendto(domain_IP.encode(), client_info)

    elif domain_name in CNAME_records:
        CNAME = CNAME_records[domain_name]
        if CNAME in A_records:
            domain_IP = A_records[CNAME]
            server_socket.sendto(domain_IP.encode(), client_info)
        else:
            server_socket.sendto(("Domain does not exist in A records").encode(), client_info)
        
    else:
        server_socket.sendto(("Domain does not exist!").encode(), client_info)
        
server_socket.close()