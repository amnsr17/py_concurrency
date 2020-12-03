import os, sys
import multiprocessing
import traceback

class MyProcess(multiprocessing.Process):
    # constructor
    def __init__(self, pipe_in):
        multiprocessing.Process.__init__(self)
        self.pipe_in = pipe_in

    def run(self):
        try:
            raise Exception("This thing broke stuff")
        except:
            except_type, except_class, tb = sys.exc_info()

        self.pipe_in = os.fdopen(self.pipe_in, 'w')
        self.pipe_in.write(str(except_type))
        # cloding file object
        self.pipe_in.close()

def main():
    # A pipe has two mouths so initialize on pipe with two ends: pipe_in and pipe_out
    pipe_out, pipe_in = os.pipe()

    child_process = MyProcess(pipe_in)
    child_process.start()
    child_process.join()

    # closing the pipe_in object
    os.close(pipe_in)

    # opening up this side of pipe for file reading
    pipe_out = os.fdopen(pipe_out, 'r')
    read_pipe_content = pipe_out.read()
    print("Exception : {}".format(read_pipe_content))

if __name__ == '__main__':
    main()