'''クライアント'''
import socket
import time

HOST = '127.0.0.1'
PORT = 50007

class Client:
    '''クライアントの動き'''
    def __init__(self):
        self.client = None

    def __del__(self):
        self.client.close()

    def connect(self):
        '''接続処理'''
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        print('Connected to server. IP:', HOST, 'Port:', PORT)

    def send_data(self, send_time):
        '''データの送信処理'''
        self.client.sendall(str(send_time).encode('utf-8'))

    def receive_data(self):
        '''データの受信処理'''
        received_data = self.client.recv(1024).decode('utf-8')
        print(f'received data : {received_data}')

instance = Client()

while True:
    instance.connect()
    instance.send_data(time.time_ns())
    instance.receive_data()

    time.sleep(2.0)
