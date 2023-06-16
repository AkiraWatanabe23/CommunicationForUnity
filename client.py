'''受信側'''
import socket

PORT = 3123

cliesock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliesock.connect((socket.gethostname(), PORT))

cliesock.send(b'hello, world!')

data = cliesock.recv(1024)
print(data)

cliesock.close()
