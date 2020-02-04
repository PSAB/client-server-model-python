import socket

class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '10.143.54.151'
        self.port = 5555
        self.address = (self.server, self.port)
        # self.connect()
        self.position = self.connect()

    def getPosition(self):
        return self.position

    def connect(self):
        try:
            self.client.connect(self.address)
            # recv = self.client.recv(2048).decode()
            # print(recv)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

