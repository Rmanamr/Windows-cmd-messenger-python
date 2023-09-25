"""A simple windows cmd messenger"""

# TCP server

import time
import socket
import threading

# defining IP address and port
connection = ('localhost', 12345)

# initialize a socket object using IPv4 and TCP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding 
server.bind(connection)

# limiting count of connected clients
server.listen(2)
 
# con variable for sending data and addr variable for the address of connected client
connect, address = server.accept()

# function to send data
def send_Data():
    while True:
        data = input(">> ")
        if data != "":
            connect.send(data.encode())
            time.sleep(0.1)

# function to receive data
def receive_Data():
    while True:
        # store every 1024 characters
        data = connect.recv(1024)
        print(" : " + data.decode())
        time.sleep(0.1)

# set the threads
threading.Thread(target = receive_Data).start()
threading.Thread(target = send_Data).start()


# by Arman Azarnik
# armanazarnik@gmail.com