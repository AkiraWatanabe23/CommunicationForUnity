'''送信側(TCP) ... 送信時のエポック秒を送信する'''
import socket
import os
import time
import keyboard

HOST = '127.0.0.1'
MAINPORT = 50007

def connect_unity():
    '''Unityにデータを送る'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #os.getpid() ... プロセスIDの取得
    print(os.getpid())

    #Unityに接続
    client.connect((HOST, MAINPORT))

    #データを送信する
    client.send(str(time.time_ns()).encode('utf-8'))

    #送信時の時間（エポック秒）
    print(time.time_ns())

    #データを受信する
    #1024 ... 受信するデータのバイト数（この数値以下のバイト数のデータなら、問題なく実行される）
    data = client.recv(1024)
    print(data.decode('utf-8'))

    if keyboard.is_pressed('s'):
        client.close()

    #2秒待つ
    time.sleep(2.0)

    return client

while True:
    connect_unity()
