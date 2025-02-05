# >>>>>>>>>> Locks In Threading <<<<<<<<<< (5)
from threading import Thread, Lock
import time

lock = Lock()

value = 10
def f1():
    with lock:
        global value
        time.sleep(2)
        x = 10
        x += value
        print(x)

def f2():
    with lock:
        global value
        value = 12

t1 = Thread(target=f1)
t2 = Thread(target=f2)

t1.start()
t2.start()
