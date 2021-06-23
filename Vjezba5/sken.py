import socket
import datetime
print("Program se izvodi:")
print(datetime.datetime.now())
from local_machine_info import print_machine_info
print_machine_info()
print("----------------------------------------------")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input("Unesite adresu hosta: ")
print("Skeniram adresu: ",target)

print("od kojeg do kojeg porta ?")

p1 = input("Prvi port => ")
p2 = input("Drugi port => ")

p1 = int(p1)
p2 = int(p2)

def scanner(port):
    try:
        sock.connect((target,port))
        return True
    except:
        return False

for portNumber in range(p1,p2):
    print("Skeniram port", portNumber)
    if scanner(portNumber):
        print('Port: ',portNumber,'/tcp',' je otvoren!')