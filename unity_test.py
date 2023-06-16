'''送信側(TCP)'''
import socket
import os

HOST = "127.0.0.1"
MAINPORT = 50007

def connect_unity():
    '''データ送信'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = str(os.getpid())
    print(os.getpid())

    client.connect((HOST, MAINPORT))

    client.send(result.encode('utf-8'))

    data = client.recv(200)

    print(data.decode('utf-8'))

    return client
