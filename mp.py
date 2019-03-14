import multiprocessing as mp
import os
import psutil

def g(x):
    return x*x

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)


# if __name__ == '__main__':
#     with mp.Pool(5) as p:
#         print(p.map(g, [1, 2, 3]))

#     print(mp.cpu_count())
#     print(os.sched_getaffinity(0))
#     print(psutil.cpu_count(logical=False))


# if __name__ == '__main__':
#     info('main line')
#     p = mp.Process(target=f, args=('bob',))
#     p.start()
#     p.join()

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()    