"""A simple windows cmd messenger"""

# TCP client

import time
import socket
import threading

# defining IP address and port
connection = ('localhost', 12345)

# initialize a socket object using IPv4 and TCP protocol
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# coccnecting to server
client.connect(connection)

# function to send data
def send_Data():
    while True:
        data = input(">> ")
        if data != "":
            client.send(data.encode())
            time.sleep(0.1)

# function to receive data
def receive_Data():
    while True:
        # store every 1024 characters
        data = client.recv(1024)
        print(" : " + data.decode())
        time.sleep(0.1)

# set the threads
threading.Thread(target = receive_Data).start()
threading.Thread(target = send_Data).start()


# by Arman Azarnik
# armanazarnik@gmail.com