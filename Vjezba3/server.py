import socket
server_socket = socket.socket()
host = socket.gethostname()
port = 9999
server_socket.bind((host,port))
print ("Waiting for connection...")
server_socket.listen(5)
while True:
 conn,addr = server_socket.accept()
 print ('Got Connection from', addr)
 conn.send('Server Saying Hello'.encode())
 conn.close() 