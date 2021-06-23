import queue
import threading
import time
import datetime
print("Program se izvodi na ovom racunalu:")
print(datetime.datetime.now())

from local_machine_info import print_machine_info

print_machine_info()
print("----------------------------------------------")

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("Pokrecem nit " + self.name)
        process_data(self.name, self.q)
        print ("Izlazim iz niti " + self.name)
def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s procesuira %s" % (threadName, data))
        else:
            queueLock.release()
            time.sleep(1)
            
threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["Jedan", "Dva", "Tri", "Cetiri", "Pet"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()
print ("\nIzlazim iz glavne niti\n")