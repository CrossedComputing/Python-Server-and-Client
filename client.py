import socket

class Client:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))
    
    def sendMessage(self, message):
        self.sock.sendall(message)


if __name__ == "__main__":
    client = Client("127.0.0.1", 1337)
    client.connect()
    client.sendMessage(b"Hello, Server!")