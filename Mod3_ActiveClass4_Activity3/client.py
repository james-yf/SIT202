import socket

server_info = ('localhost', 11124)
response_buff = 100
send_message = 'y'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        if send_message == 'n':
            break
        
        message = input("Enter a message: ")
        client_socket.sendto(message.encode(), server_info)
        response_message, _ = client_socket.recvfrom(response_buff)
        print(f"The server responded with: [{response_message.decode()}]")

        send_message = input("\nDo you want to send another message? (y/n): ")

# terminate the server program if there is an exception or user entered 'n'.
finally:
    print("The client program is terminating...")
    client_socket.sendto(("terminate").encode(), server_info)
    client_socket.close()


