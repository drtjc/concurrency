import threading

lock = threading.RLock()
def CountDown(n):
    
    with lock:
        while True:
            t = threading.current_thread()
            msg = f'thread: {t}, n = {n}'
            print(msg)
            n -= 1
            if n == 0:
                break

n = 5
for i in range(2):
    t = threading.Thread(target = CountDown, args = (n,))
    t.start()

#CountDown(n)



