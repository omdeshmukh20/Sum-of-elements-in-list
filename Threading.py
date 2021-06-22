#Discription: Threading
#Date: 22/06/21
#Author : Om Deshmukh

import os
import threading
from time import sleep

def Thread1(no):
    print("Thread1 is created")
    print("PID of Thread1 is : ",os.getpid())
    for i in range(no):
        sleep(1)
        print("Thread-1 ",i)

def Thread2(no):
    print("Thread1 is created")
    print("PID of Thread1 is : ",os.getpid())
    for i in range(no):
        sleep(1)
        print("Thread-2 ",i)

def main():
    print("Inside main thread")
    print("PID of main process is :",os.getpid())
    print("PID of parent process of main is :",os.getppid())
    value = 10
    t1 = threading.Thread(target = Thread1, args = (value,))
    t2 = threading.Thread(target = Thread2, args = (value,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("End of main thread")
    
if __name__ == "__main__":
    main()
