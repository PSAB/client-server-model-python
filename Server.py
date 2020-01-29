import socket
from  _thread import *
import sys

server = "" # IP Address here
port = 5555 # Safe port to use

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Bind the server to specified IP Address
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen() # Expecting websocket connections

print('waiting for connection, server started')

def threaded_client(connection):
    reply = ""
    while True:
        try:
            data = connection.recv(2048) # Bit size to send and receive over websocket
            reply = data.decode('utf-8') # decode the transmitted bits of information

            if not data:
                print('Disconnected')
                break

        except:
            pass


while True:
    # Accept any incoming connections, store in connection object and store ip as well
    connection, address = s.accept()
    print('Connected to address: ', str(address))

    # Begin the threaded_client function in a second background thread while this while loop is still running
    start_new_thread(threaded_client, (connection, ))