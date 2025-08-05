import socket

server_info = ('localhost', 11124)
message_buff = 100

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_info)

print("The server is running!")

while True:
    _, client_info = server_socket.recvfrom(message_buff)
    message = _.decode()
    
    if message == "terminate":
        print("The server program is terminating...")
        break

    char_count = len(message)
    uppercase_message = message.upper()
    response_message = str(char_count) + " " + uppercase_message

    print(f"{char_count}")
    server_socket.sendto(response_message.encode(), client_info)
    
server_socket.close()