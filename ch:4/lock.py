import threading
import time
import random

# we'll place a lock for changing the value of the counter
counter = 1

lock = threading.Lock()

def workerA():
    # introducing the counter which is outside the scope as global variable
    global counter
    lock.acquire()
    try:
        while counter < 10:
            counter += 1
            print("Worker A is incrementing counter to {}".format(counter))
            sleepTime = random.randint(0, 1)
            time.sleep(sleepTime)
    finally:
        lock.release()

def workerB():
    # introducing the counter which is outside the scope as global variable
    global counter
    lock.acquire()
    try:
        while counter > -10:
            counter -= 1
            print("Worker B is decrementing counter to {}".format(counter))
            sleepTime = random.randint(0, 1)
            time.sleep(sleepTime)
    finally:
        lock.release()

def main():
    t0 = time.time()
    thread1 = threading.Thread(target=workerA)
    thread2 = threading.Thread(target=workerB)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    t1 = time.time()
    print("Execution Time {}".format(t1-t0))

if __name__ == '__main__':
    main()
