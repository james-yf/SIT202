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

# creates and returns the socket
def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(server_info)
    return s

# gets the domain name from the query and returns it
def get_domain_name(server_socket):
    query_buff = 100
    query, client_info = server_socket.recvfrom(query_buff)
    domain_name = query.decode()
    return (domain_name, client_info)

# checks if there is any records of the domain name
def domain_lookup(server_socket, domain_name, client_info):
    if domain_name in A_records:
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

def main():
    server_socket = create_socket()
    print("The server is running and awaiting a query from the client!")

    while True:
        (domain_name, client_info) = get_domain_name(server_socket)
        print(f"Server received the DNS query for [{domain_name}] from the client.")
        
        if domain_name == "terminate":
            print("The server program is terminating...")
            server_socket.close()
            return
        else:
            domain_lookup(server_socket, domain_name, client_info)

if __name__=="__main__":
    main()