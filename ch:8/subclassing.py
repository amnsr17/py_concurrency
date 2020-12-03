import multiprocessing
import os

class MyProcess(multiprocessing.Process):
    def __init__(self):
        # same way of calling parent class constructor
        # super(MyProcess, self).__init__()
        multiprocessing.Process.__init__(self)
    def run(self):
        print("Child Process PID: {}".format(multiprocessing.current_process().pid))

def main():
    print("Main Process PID: {}".format(multiprocessing.current_process().pid))
    myProcess = MyProcess()
    myProcess.start()
    myProcess.join()

    # following code will spin up processes equal to the
    # number of cpu cores avilable of this PC
    processes = []
    for i in range(os.cpu_count()):
        process = MyProcess()
        processes.append(process)
        process.start()

    print(len(processes))


if __name__ == '__main__':
    main()