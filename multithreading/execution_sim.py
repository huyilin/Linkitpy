__author__ = 'Yilin'

from threading import Timer
import time
from threading import Lock

lock = Lock()

class Test:

    def __init__(self):
        self.hi = 'dwfw'

    def f(self, a, b):
        hi = a
        with lock:
            print hi
            time.sleep(b)

test = Test()
timer1 = Timer(0.1, test.f, ['a',0])
timer2 = Timer(0.1, test.f, ['b',0])
# timer3 = Timer(3, test.f, ['c',2])
timer1.start()
timer2.start()
# timer3.start()