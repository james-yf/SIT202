import socket

server_addr = 'localhost'
server_port = 11124
response_buff = 100
send_query = 'y'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        if send_query == 'n':
            break
        
        domain_name = input("Enter a domain name: ")
        client_socket.sendto(domain_name.encode(), (server_addr, server_port))
        server_response, server_info = client_socket.recvfrom(response_buff)
        print(f"The server responded with: {server_response.decode()}")

        send_query = input("\nDo you want to send another DNS query? (y/n): ")
finally:
    print("The client program is terminating...")
    # tell the server program to terminate
    client_socket.sendto(("terminate").encode(), (server_addr, server_port))
    client_socket.close()