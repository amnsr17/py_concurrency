import threading
import time
import random


"""
    we are going to utilize barriers in order to block the
    execution of our threads until all of the threads have reached a desired point
    of execution.
"""

class MyThread(threading.Thread):

    # constructor
    def __init__(self, barrier):
        # initialize data member
        self.barrier =barrier
        # parent class constructor call
        threading.Thread.__init__(self)

    def run(self):
        print("Thread {} working on something.".format(threading.current_thread()))
        time.sleep(random.randint(0,1))
        print("Thread {} is joining {} waiting on the Barrier.".format(threading.current_thread(),self.barrier.n_waiting))
        # to wait on the barrier until all threads have called this method
        self.barrier.wait()
        print("Barrier has been lifted, continuing with work.")

def main():
    # making a barrier for 4 threads
    barrier = threading.Barrier(4)

    threads = []

    for i in range(4):
        thread = MyThread(barrier)
        thread.start()
        threads.append(thread)

    # joining the threads so that main thread wait until all are joined
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()



