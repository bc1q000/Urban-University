import time
from threading import Thread, Lock
from datetime import datetime

# Версии ниже Python 3.10 не вычисляют выражение x = x + i атомарно
t_start = datetime.now()
x = 0
def thread_task():
    global x
    for i in range(10_000_000):
        x += 1
def main():
    global x
    x = 0
    t1 = Thread(target=thread_task())
    t2 = Thread(target=thread_task())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

for i in range(10):
    main()
    print(x)
t_end = datetime.now()
print(f'{t_end - t_start}')


# Версия с блокировкой
t_start = datetime.now()
lock = Lock()
x = 0
def thread_task():
    global x
    for i in range(10_000_000):

        # lock.acquire()
        # x += 1
        # lock.release()

        # with lock:
        #     x += 1

        try:
            lock.acquire()
            x += 1
        finally:
            lock.release()
def main():
    global x
    x = 0
    t1 = Thread(target=thread_task())
    t2 = Thread(target=thread_task())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

for i in range(10):
    main()
    print(x)
t_end = datetime.now()
print(f'{t_end - t_start}')


# Взаимная блокировка (программа намеренно работает не до конца)
# Потоки блокируют друг друга
# Эту проблему нужно опасаться
lock1 = Lock()
lock2 = Lock()

def thread_task1():
    lock1.acquire()
    print('thread 1 lock1 acquire')
    time.sleep(1)
    lock2.acquire()
    print('thread 1 lock2 acquire')
    lock2.release()
    lock1.release()

def thread_task2():
    lock2.acquire()
    print('thread 2 lock2 acquire')
    time.sleep(1)
    lock1.acquire()
    print('thread 2 lock1 acquire')
    lock1.release()
    lock2.release()

t1 = Thread(target=thread_task1)
t2 = Thread(target=thread_task2)

t1.start()
t2.start()

t1.join()
t2.join()