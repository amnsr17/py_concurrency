import os
import sys
import multiprocessing

"""
    implementing of OS Pipes which are simplex pipes
"""
class ChildProcess(multiprocessing.Process):
    # constructor calling parent class constructor
    def __init__(self, pipe_in):
        multiprocessing.Process.__init__(self)
        # data member
        self.pipe_in = pipe_in

    def run(self):
        print("Attempting to pip-in to the pipe")
        # opening os level file object which is created using os.fdopen()
        self.pipe_in = os.fdopen(self.pipe_in,'w')
        self.pipe_in.write("My Name is Elliot")
        self.pipe_in.close()

def main():
    # made two pipes
    pipeout, pipein = os.pipe()
    # passed one side of the pipe to the child process
    child = ChildProcess(pipein)

    child.start()
    # forcing the parent process to wait for the exit of the child process
    child.join()
    # closing the pipe
    os.close(pipein)

    pipeout = os.fdopen(pipeout)
    pipeContent = pipeout.read()
    print("Pipe: {}".format(pipeContent))


if __name__ == '__main__':
    main()
