import socket
import threading
import datetime
pocetak = datetime.datetime.now()
from queue import Queue
print("Program se izvodi na ovom racunalu:")
print(datetime.datetime.now())

from local_machine_info import print_machine_info

print_machine_info()
print("----------------------------------------------")

print_lock = threading.Lock()

target = input("Unesite adresu hosta kojeg zelite skenirati: ")
print("Skeniram adresu: ",target)

print("Unesite od kojeg do kojeg porta zelite skenirati...")

p1 = input("Prvi port => ")
p2 = input("Drugi port => ")

p1 = int(p1)
p2 = int(p2)

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('Port' , port, ' je otvoren!!!')
        con.close()
    except:
        pass
def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(p1,p2):
    q.put(worker)

q.join()

kraj = datetime.datetime.now()
print('Vrijeme potrebno za izvedbu: {}'.format(kraj - pocetak))



