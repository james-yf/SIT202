import socket

# (alias name : canonical name)
CNAME_records = {
    "blog.pamelabeesly.com": "pamelabeesly.com",
    "www.pamelabeesly.com": "pamelabeesly.com",
    "blog.jimhalpert.com": "jimhalpert.com",
    "www.jimhalpert.com": "jimhalpert.com",
    "blog.michaelscott.com": "michaelscott.com",
    "www.michaelscott.com": "michaelscott.com"
}

# (canonical name : IP address)
A_records = {
    "pamelabeesly.com": "45.67.89.123",
    "jimhalpert.com": "102.154.76.88",
    "michaelscott.com": "172.32.210.5"
}

server_addr = 'localhost'
server_port = 11124
request_buff = 100

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((server_addr, server_port))

while True:
    # client_info is a tuple: (IP address, Port number)
    encoded_domain_name, client_info = server_socket.recvfrom(request_buff)

    domain_name = encoded_domain_name.decode()

    if domain_name in A_records:
        domain_addr = A_records[domain_name]
        server_socket.sendto(domain_addr.encode(), client_info)
    elif domain_name in CNAME_records:
        domain_addr = A_records[CNAME_records[domain_name]]
        server_socket.sendto(domain_addr.encode(), client_info)
    elif domain_name == "terminate":
        print("The server program is terminating...")
        break
    else:
        server_socket.sendto(("Domain does not exist!").encode(), client_info)
        
server_socket.close()