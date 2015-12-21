__author__ = 'Yilin'

from threading import Timer
import time

def foo():
    print "hello this is true"


timer = Timer(3, foo)
timer.start()
time.sleep(6)

timer.cancel()