import multiprocessing
import time

def myProcess():
    current_process = multiprocessing.current_process()
    print("Child Process PID: {}".format(current_process.pid))
    time.sleep(20)

def main():
    # This code shows that using terminate kills child process and do not let it wait
    # for 20 seconds as it was supposed to wait.

    current_process = multiprocessing.current_process()
    print("Main process PID: {}".format(current_process.pid))

    my_process = multiprocessing.Process(target=myProcess)
    my_process.start()

    print("My Process has terminated, terminating main thread")

    print("Terminating Child Process")
    my_process.terminate()

    print("Child Process Successfully terminated")

if __name__ == '__main__':
    main()