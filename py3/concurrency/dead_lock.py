import threading
import time

m1 = threading.Lock()
m2 = threading.Lock()


def func1():
    m1.acquire()
    time.sleep(0.1)
    m2.acquire()
    m1.release()
    m2.release()


def func2():
    m2.acquire()
    time.sleep(0.1)
    m1.acquire()
    m2.release()
    m1.release()


import threading

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()
t1.join()
t2.join()
print("Will not get here, should release lock before getting another one")
