import threading
import time

lock = threading.RLock()
def CountDown(n):
    
    with lock:
        while True:
            t = threading.current_thread()
            msg = f'thread: {t}, n = {n}'
            print(msg)
            time.sleep(1)
            n -= 1
            if n == 0:
                break

n = 5
for i in range(2):
    t = threading.Thread(target = CountDown, args = (n,))
    t.start()

ts = threading.enumerate()
for t in ts:
    print(f'threads: {t.name}')

ts[1].join()
print(f'active threads: {threading.active_count()}')
ts[2].join()
print(f'active threads: {threading.active_count()}')


#CountDown(n)

import random

class MyLocal(threading.local):
    def __init__(self, v):
        self.val = v


def f(d):
    t = threading.current_thread()
    print(f't:{t.name}; val = {d.val}')
    d.val = random.randint(1, 100)
    time.sleep(1)
    print(f't:{t.name}; val = {d.val}')

# d = MyLocal(999)

# for i in range(2):
#     t = threading.Thread(target = f, args = (d,))
#     t.start()


class MyGlobal():
    def __init__(self, v):
        self.val = v
    
d = MyGlobal(999)

for i in range(2):
    t = threading.Thread(target = f, args = (d,))
    t.start()
