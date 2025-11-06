from threading import Thread, Condition
from time import sleep

class MyData:
    def __init__(self):
        self.data = None
        self.cv = Condition()

    def put(self, d):
        with self.cv:
            while self.data is not None:
                self.cv.wait()

            self.data = d
            print('Producer:', d)

            self.cv.notify()

    def get(self):
        with self.cv:
            while self.data is None:
                self.cv.wait()

            x = self.data
            self.data = None
            print('Consumer:', x)

            self.cv.notify()
            return x

def producer(mydata):
    i = 1
    while True:
        mydata.put(i)
        i += 1
        sleep(1)

def consumer(mydata):
    while True:
        x = mydata.get()
        sleep(1)

mydata = MyData()
t1 = Thread(target=lambda:producer(mydata))
t2 = Thread(target=lambda:consumer(mydata))

t1.start()
t2.start()


t1.join()
t2.join()