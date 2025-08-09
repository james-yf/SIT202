import socket
client_info = ('localhost', 11125)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(client_info)

message_buff = 100
server_socket.listen(1)
print("The server is listening!")
connectCl1Socket, _ = server_socket.accept()
print("Connection established")

while True:
    message = connectCl1Socket.recv(message_buff)
    message = message.decode()
    
    if message == "terminate":
        print("The server program is terminating...")
        break

    len_message = len(message)
    print(len_message)
    response_message = str(len(message)) + ": " + message.upper()
    connectCl1Socket.sendall(response_message.encode())

connectCl1Socket.close()
server_socket.close()

