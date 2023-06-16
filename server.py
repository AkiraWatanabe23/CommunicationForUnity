'''受信側'''
import socket

PORT = 3123

servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servsock.bind((socket.gethostname(), PORT))

servsock.listen()

while True:
    print("accept...")
    clisock, addr = servsock.accept()

    data = clisock.recv(1024)
    print(data)

    clisock.send(b'ok')

    clisock.close()
