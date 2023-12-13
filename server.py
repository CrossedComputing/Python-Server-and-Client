import socket


class Server:
    buffer_size = 1024

    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
    
    def startServer(self):
        try:
            # AF_INET = address family for IPv4
            # SOCK_STREAM = TCP Protocol
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Bind the ip and port to the socket
            self.sock.bind((self.ip, self.port))

            # Listen for a connection
            self.sock.listen()

            # Wait and accept a connection
            self.conn, self.connectedAddress = self.sock.accept()
        except:
            print("Something went wrong with creating a socket. Please check the IP address and port")

    def listen(self):
        print(f"[{self.connectedAddress[0]}, connected]")

        while(True):
            # Put the bytes recieved from the client in a buffer of bytes
            buffer = self.conn.recv(self.buffer_size)

            # If an empty byte array is recieved, break
            if buffer == b'':
                break
            # Print the bytes recieved as a string
            else:
                print(f"{self.connectedAddress[0]} sent: {buffer.decode()}")


if __name__ == "__main__":
    server = Server("127.0.0.1", 1337)
    server.startServer()
    server.listen()
