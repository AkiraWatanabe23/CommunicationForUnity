'''送信側(UDP)'''
import socket
import random
import time
import keyboard

times = []

HOST = '127.0.0.1'
PORT = 50007

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    if keyboard.is_pressed('s'):
        break

    n = random.randrange(3)
    result = str(n)
    #print(n)

    send_time = time.time_ns()
    times.append(send_time)
    print(send_time)

    client.sendto(result.encode('utf-8'), (HOST, PORT))
    time.sleep(2.0)
