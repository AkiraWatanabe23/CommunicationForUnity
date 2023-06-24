'''クライアント'''
import socket
import time

HOST = '127.0.0.1'
PORT = 50007

def data_client():
    '''クライアントの働きをする'''
    #接続
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print('Connected to server. IP:', HOST, 'Port:', PORT)

    #送信
    data_to_send = str(time.time_ns())
    client.sendall(data_to_send.encode('utf-8'))

    #応答を受け取る
    received_data = client.recv(1024).decode('utf-8')
    print('Received data:', received_data)

    client.close()
    time.sleep(2.0)

while True:
    data_client()
