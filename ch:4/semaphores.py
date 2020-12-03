# It is a ticket selling program that features four distinct threads that each try to sell as
# many tickets of the entire ticket allocation as they can before the tickets are
# sold out.

import threading
import time
import random


class TicketSeller(threading.Thread):
    # This class contains it's own
    # internal counter for how many tickets that it has sold.
    ticketsSold = 0

    # Constructor - takes a semaphore as parameter
    def __init__(self, semaphore):

        # data members
        self.sem = semaphore

        # calling parent class constructor for thread generation
        threading.Thread.__init__(self)
        print("The TicketSeller has started working")

    def run(self):
        global ticketsAvailable
        running = True
        while running:
            time.sleep(random.randint(0,1))
            # acquire semaphore
            self.sem.acquire()

            if ticketsAvailable<=0:
                running = False
            else:
                self.ticketsSold += 1
                ticketsAvailable -= 1
                print("{} Sold One ({} left)".format(self.getName(), ticketsAvailable))

            self.sem.release()
        print("Ticket Seller {} Sold {} tickets in total".format(self.getName(), self.ticketsSold))


def main():
    # our sempahore primitive
    semaphore = threading.Semaphore()

    # Our Ticket Allocation
    global ticketsAvailable
    ticketsAvailable = 10

    # our array of sellers
    sellers = []

    for i in range(4):
        seller = TicketSeller(semaphore)
        seller.start()
        sellers.append(seller)

    # joining all our sellers
    for seller in sellers:
        seller.join()

if __name__ == '__main__':
    main()








