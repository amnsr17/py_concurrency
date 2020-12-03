import multiprocessing

"""
    Implements python pipes not fromm OS package but from multiprocessing package.
    These pipes are duplex by default.
"""

def my_f(conn):
    # sending information to the child connection side of the pipe
    conn.send([42, None, 'hello'])
    conn.close()

def main():
    # making two pipe connections
    parent_conn, child_conn = multiprocessing.Pipe()
    # making a child processs and
    my_process = multiprocessing.Process(target=my_f, args=(child_conn,))
    my_process.start()
    # receiving the information from this end of pipe.
    print(parent_conn.recv())   # prints "[42, None, 'hello']"

    my_process.join()

if __name__ == '__main__':
    main()