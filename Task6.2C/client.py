import socket

"""tuple containing IP and Port#"""
server_info = ('localhost', 11124)
response_buff = 100
send_query = 'y'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        if send_query == 'n':
            break
        
        domain_name = input("Enter a domain name: ")
        client_socket.sendto(domain_name.encode(), server_info)
        server_response, _ = client_socket.recvfrom(response_buff)
        print(f"The server responded with: {server_response.decode()}")

        send_query = input("\nDo you want to send another DNS query? (y/n): ")

# terminate the server program if there is an exception
finally:
    print("The client program is terminating...")
    client_socket.sendto(("terminate").encode(), server_info)
    client_socket.close()