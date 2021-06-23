import socket
client_socket = socket.socket()
host = socket.gethostbyname('www.google.hr')
port = 80

client_socket.connect((host,port))
print ('Socket se spojia na google port = ',port,' i IP  = ',host)

client_socket.close()