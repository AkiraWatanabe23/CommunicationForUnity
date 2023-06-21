'''送信側(TCP)'''
import socket
import os
import time
import keyboard

HOST = '127.0.0.1'
MAINPORT = 50007

SEND_TIME = 0

def connect_unity():
    '''Unityにデータを送る'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if keyboard.is_pressed('s'):
        client.close()

    #result = str(os.getpid())
    print(os.getpid())

    client.connect((HOST, MAINPORT))

    #client.send(result.encode('utf-8'))
    client.send(str(time.time_ns()).encode('utf-8'))

    print(time.time_ns())

    data = client.recv(200)

    print(data.decode('utf-8'))

    return client

while True:
    connect_unity()
