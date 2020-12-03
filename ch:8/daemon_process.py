import multiprocessing
import time

def daemon_process():
    print("starting my daemon process")
    print("Daemon process started: {}".format(multiprocessing.current_process()))
    time.sleep(5)
    print("Daemon process terminating")
    # print("Main process: {}".format(multiprocessing.current_process()))

def main():
    my_process = multiprocessing.Process(target=daemon_process)
    my_process.daemon = True
    my_process.start()
    # this is a daemon process - so no need to join it as it will be
    # terminated with the termination of the main process

    for i in range(20):
        print("Main process is running")
        time.sleep(2)

if __name__ == '__main__':
    main()