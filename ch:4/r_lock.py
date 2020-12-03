import threading
import time

# Defining a Class
class myWorker():
    # constructor
    def __init__(self):
        # initilizes the data-members
        self.a = 1
        self.b = 2
        self.Rlock = threading.RLock()

    # class methods:
    #   modifyA()
    #   modifyB()
    #   modifyBoth()

    def modifyA(self):
        # acquires Rlock
        with self.Rlock:
            # Then modifies the internal variable
            print("Modifying A, Rlock acquired: {}".format(self.Rlock._is_owned()))
            print("{}".format(self.Rlock))
            self.a = self.a + 1
            time.sleep(5)

    def modifyB(self):
        # acquires Rlock
        with self.Rlock:
            # Then modifies the internal variable
            print("Modifying B, Rlock acquired: {}".format(self.Rlock._is_owned()))
            print("{}".format(self.Rlock))
            self.a = self.b + 1
            time.sleep(5)

    def modifyBoth(self):
        # acquires Rlock
        with self.Rlock:
            # Then calls the two above functions to change the internal variables/datamembers
            print("Rlock acquired, Modifying both A and B")
            print("{}".format(self.Rlock))
            self.modifyA()

            # print("{}".format(self.Rlock))
            for i in range(2):
                self.modifyA()
                print("{}".format(self.Rlock))

            print("{}".format(self.Rlock))
            self.modifyA()
            print("{}".format(self.Rlock))
            self.modifyB()
            print("{}".format(self.Rlock))
        print("{}".format(self.Rlock))
        # At this point (when we exit this modifyBoth function) the count of RLock becomes zero -
        # only at this point any other thread can acquire it
        # A second advantage of using RLocks is that we do not have to release the lock using lock.realease.


def main():
    # instantiating an object of class myWorker
    workerA = myWorker()
    workerA.modifyBoth()


if __name__ == '__main__':
    main()
