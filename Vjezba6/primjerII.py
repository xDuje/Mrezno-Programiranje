import threading
import time
import datetime
print("Program se izvodi na ovome racunalu:")
print(datetime.datetime.now())

from local_machine_info import print_machine_info

print_machine_info()
print("---------------------------------")
exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
def run(self):
    print ("Pokrecem nit " + self.name)
    print_time(self.name, 5, self.counter)
    print ("Izlazim iz niti " + self.name)
def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
           threadName.exit()
           time.sleep(delay)
           print("%s: %s" % (threadName, time.ctime(time.time())))
           counter -= 1
# Kreiraj nove niti
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
# Pokreni nove niti
thread1.start()
thread2.start()
print ("\nIzlazim iz glavne niti\n")
