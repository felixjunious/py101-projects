from threading import Thread, Lock
from time import sleep

class MyData:
    def __init__(self):
        self.data = None
        self.flag = False
        self.lock = Lock()

    def put(self, d):
        while self.flag != False:
            pass
        self.lock.acquire()
        self.data = d
        self.flag = True
        self.lock.release()
        sleep(1)

    def get(self):
        while self.flag != True:
            pass
        self.lock.acquire()
        x = self.data
        self.flag = False
        self.lock.release()
        sleep(1)
        return x

def producer(mydata):
    i = 1
    while True:
        mydata.put(i)
        print('Producer:', i)
        i += 1

def consumer(mydata):
    while True:
        x = mydata.get()
        print('Consumer:', x)

mydata = MyData()
t1 = Thread(target=lambda:producer(mydata))
t2 = Thread(target=lambda:consumer(mydata))

t1.start()
t2.start()

t1.join()
t2.join()