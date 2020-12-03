

import threading
import time

"""
    something is not right on my system, the main thread is not getting the chance of running my_event.set() instruction
"""


def my_thread(my_event):
    while not my_event.is_set():
    # while my_event.is_set() != True:
    # while my_event.is_set() is False:
        print("waiting for the event to be set.")
        time.sleep(1)
    print("event has been set")

def main():
    # Making Event
    my_event = threading.Event()

    # Making thread
    thread1 = threading.Thread(target=my_thread(my_event), args=(my_event,))
    thread1.start()
    print("Now sleeping")
    # time.sleep(3)
    my_event.set()

if __name__ == '__main__':
    main()



