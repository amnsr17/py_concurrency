# We are going to create two different classes that will inherit
# from the thread class. These will be our Publisher and our subscriber classes.
# The publisher will do the task of publishing new integers to an integer array,
# and then notifying the subscribers that there is a new integer to be consumed
# from the array
import threading
import random
import time

class Publisher(threading.Thread):
    def __init__(self, integers, condition):
        # data members
        self.condition = condition
        self.integers = integers
        # parent class constructor being called
        threading.Thread.__init__(self)

    def run(self):
        while True:
            # randomly generate an integer b/w 0 and 1000
            integer = random.randint(0,1000)
            # acquire Condition
            self.condition.acquire()
            print("Condition acquired by the publisher: {}".format(self.name))
            # add integer to list
            self.integers.append(integer)
            # notify about the addition
            self.condition.notify()
            # releasing condition
            print("Condition released by the publisher: {}".format(self.name))
            self.condition.release()
            time.sleep(1)

class Subscriber(threading.Thread):
    def __init__(self, integers, condition):
        # data members
        self.integers =integers
        self.condition = condition
        # parent class constructor called
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.condition.acquire()
            print("Condition acquired by the consumer: {}".format(self.name))
            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print("{} Popped from list by Consumer: {}".format(integer, self.name))
                    break
                print("Condition Wait by {}".format(self.name))
                self.condition.wait()
        print("Consumer {} Releasing Condition".format(self.name))
        self.condition.release()

def main():
    integers = []
    # Instantiating the Condition
    condition = threading.Condition()
    # Our Publisher
    pub1 = Publisher(integers, condition)
    pub1.start()
    # Our Subscribers
    sub1 = Subscriber(integers, condition)
    sub2 = Subscriber(integers, condition)
    # At the point of the condition being notified, the battle starts between the two
    # subscribers where they both try to acquire this condition first. When one wins
    # this fight, it then goes on to simply "pop" this number from the array.
    sub1.start()
    sub2.start()
    ## Joining our Threads
    pub1.join()
    sub1.join()
    sub2.join()

if __name__ == '__main__':
    main()










