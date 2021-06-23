import socket
import datetime
print(datetime.datetime.now())

from local_machine_info import print_machine_info

print_machine_info()

host = socket.gethostname()
port = 12345
client_socket = socket.socket()

client_socket.connect((host,port))

client_socket.sendall('Dobar dan!'.encode())
while True:
    try:
        unos = input("Unesite rijec: ")
        if unos == 'duje_duplancic':
        	raise ValueError
    except ValueError:
        print("Nevazeci unois!")
    else:
        break

print(unos)

client_socket.close()