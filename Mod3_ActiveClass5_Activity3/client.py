import socket

server_info = ('localhost', 11125)
response_buff = 104
send_message = 'y'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_info)

try:
    while True:
        if send_message == 'n':
            break
        
        message = input("Enter a message: ")
        client_socket.sendall(message.encode())
        response_message = client_socket.recv(response_buff)
        print(f"The server responded with: [{response_message.decode()}]")

        send_message = input("\nDo you want to send another message? (y/n): ")

# terminate the server program if there is an exception or user entered 'n'.
finally:
    print("The client program is terminating...")
    client_socket.sendto(("terminate").encode(), server_info)
    client_socket.close()