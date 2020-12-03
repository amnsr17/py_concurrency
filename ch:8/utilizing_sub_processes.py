import multiprocessing
import time

"""
    just showing that we can spin up child processes using the multiprocessing module
"""

def my_process():
    print("executing child process. it has its own instance of GIL. ")
    time.sleep(5)
    print("child process ended")

def main():

    child_process = multiprocessing.Process(target=my_process)
    child_process.start()
    # if we join the child process here, it will go into waiting and the main process will not work until it is finished
    # child_process.join()

    for i in range(10):
        print("main process running")
        time.sleep(1)

    child_process.join()
    print("Now ending the main process.")

if __name__ == '__main__':
    main()