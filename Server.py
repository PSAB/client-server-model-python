import socket
from  _thread import *
import sys

server = "192.168.0.27" # Local IP Address here
port = 5555 # Safe port to use

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Bind the server to specified IP Address
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen() # Expecting websocket connections

print('waiting for connection, server started')

# Start a secondary thread to run in the background to process connections while the while loop below still simultaneously
# continues to search for new connections
def threaded_client(connection):
    # When we connect to a client:
    connection.send(str.encode("Connected")) # Send token to verify connection established
    reply = ""
    while True:
        try:
            data = connection.recv(2048) # Bit size to send and receive over websocket
            reply = data.decode('utf-8') # decode the transmitted bits of information

            if not data: # If client leaves or something
                print('Disconnected')
                break
            else:
                print('Received:', reply)
                print('Sending:', reply)

            # This line distributes the updated shape information to all connected clients
            connection.sendall(str.encode(reply)) # Send encoded bits of string message (have to decode too)

        except:
            break

    print("Lost connection, closing...")
    connection.close()

while True:
    # Accept any incoming connections, store in connection object and store ip as well
    connection, address = s.accept()
    print('Connected to address: ', str(address))

    # Begin the threaded_client function in a second background thread while this while loop is still running
    start_new_thread(threaded_client, (connection, )) # Built-in method of thread module!!