from socket import *

s = socket(type=SOCK_DGRAM)
s.bind(('localhost',5000))

while True:
    data,addr = s.recvfrom(1024)
    print(data,addr)
    s.sendto(data,addr)