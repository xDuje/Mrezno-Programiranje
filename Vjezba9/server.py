import socket
import ssl
import sys
import datetime
print("Program se izvodi na ovom racunalu:")
print(datetime.datetime.now())
from local_machine_info import print_machine_info
print_machine_info()
print("----------------------------------------------")
HOST = "127.0.0.1"
PORT = 60000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server = ssl.wrap_socket(
    server, server_side=True, keyfile="key.pem", certfile="cert.pem"
)

if __name__ == "__main__":
    server.bind((HOST, PORT))
    server.listen(0)

    while True:
        connection, client_address = server.accept()
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")