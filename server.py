'''受信側'''
import socket
import keyboard

HOST = '127.0.0.1'
PORT = 50007

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server started. Please waiting for connections...")

if keyboard.is_pressed('s'):
    server_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    print("Client connected:", client_address)

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        print(data)

    print("closeします")
    client_socket.close()
