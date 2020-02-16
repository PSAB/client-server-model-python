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

def read_position(str_):
    str_  = str_.split(',')
    return int(str_[0]), int(str_[1])

def make_position(tuple_):
    return str(tuple_[0]) + ',' + str(tuple_[1])

positions = [(0,0), (100,100)] # Keep track of the 2 rectangle positions

# Start a secondary thread to run in the background to process connections while the while loop below still simultaneously
# continues to search for new connections
def threaded_client(connection, currentPlayer):
    # When we connect to a client:
    # connection.send(str.encode("Connected")) # Send token to verify connection established
    connection.send(str.encode(make_position(positions[currentPlayer]))) # Send out starting positions to rectangles
    reply = ""
    while True:
        try:
            data = read_position(connection.recv(2048).decode()) # Update the position on the server
            positions[currentPlayer] = data # Re-assign that position to the current rectangle

            # reply = data.decode('utf-8') # decode the transmitted bits of information

            if not data: # If client leaves or something
                print('Disconnected')
                break
            else:
                if currentPlayer == 1: # If we're rectangle 1, send rectangle 0's positions
                    reply = positions[0]
                else:
                    reply = positions[1] # If we're rectangle 0, send rectangle 1's positions
                print('Received:', reply)
                print('Sending:', reply)

            # This line distributes the updated shape information to all connected clients
            connection.sendall(str.encode(make_position(reply))) # Send encoded bits of string message (have to decode too)

        except:
            break

    print("Lost connection, closing...")
    connection.close()


currentPlayer = 0
while True:
    # Accept any incoming connections, store in connection object and store ip as well
    connection, address = s.accept()
    print('Connected to address: ', str(address))

    # Begin the threaded_client function in a second background thread while this while loop is still running
    start_new_thread(threaded_client, (connection, currentPlayer)) # Built-in method of thread module!!
    currentPlayer += 1