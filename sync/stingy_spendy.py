import time
from threading import Thread, Lock


class StingySpendy:
    money = 100

    mutex = Lock()

    def stingy(self):
        for i in range(100000000):
            self.mutex.acquire()
            self.money += 10
            self.mutex.release()
        print("Stingy Done")

    def spendy(self):
        for i in range(100000000):
            self.mutex.acquire()
            self.money -= 10
            self.mutex.release()
        print("Spendy Done")


ss = StingySpendy()
Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()
time.sleep(45)
print("Money in the end", ss.money)

"""
I am always getting same results for the StingySpendy class even if I comment the mutex lines.
I tried executing this code many times in my mac M1 Pro, with Python 3.10.9, and I always get money = 100.
I've tried increasing the volume from 1e6 to 1e7, same.
Only when I try increasing to 1e8 I start getting different results.
"""