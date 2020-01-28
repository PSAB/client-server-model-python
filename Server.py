import socket
import _thread
import sys

server = "" # IP Address here
port = 5555 # Safe port to use

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Bind the server to specified IP Address
    s.bind((server, port))
except socket.error as e:
    print(str(e))