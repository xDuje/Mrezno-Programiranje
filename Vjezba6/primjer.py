import threading
import time
import datetime
print("Program se izvodi:")
print(datetime.datetime.now())
from local_machine_info import print_machine_info
print_machine_info()
print("------------------------------------------")

def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % ( threadName, time.ctime(time.time())))


try:
    thread.start_new_thread( print_time, ("Thread-1", 2 ))
    thread.start_new_thread( print_time, ("Thread-2", 4 ))
except:
    print("Greska: ne mogu pokrenuti !")

while 1:
    pass