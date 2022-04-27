from queue import Queue
from random import randint

now = 0


class CheckOut:
    nb_checkouts = 0
    total_waiting_time = 0
    checkouts = []

    @staticmethod
    def least_queued_checkout():
        min_checkout = CheckOut.checkouts[0]
        for c in CheckOut.checkouts:
            if c.waiting_time == 0:
                return c
            if len(c.queue) < len(min_checkout.queue):
                min_checkout = c
        return min_checkout

    @staticmethod
    def display():
        print("-" * 60)
        for i in range(len(CheckOut.checkouts)):
            print(
                f"Checkout n° {i} :  Waiting time={CheckOut.checkouts[i].waiting_time}, people waiting={len(CheckOut.checkouts[i].queue)}")
        input()

    def __init__(self, queue: Queue):
        self.ready_in = 0
        self.queue = queue
        self.waiting_time = 0
        CheckOut.nb_checkouts += 1
        CheckOut.checkouts.append(self)

    def serve(self):
        assert self.waiting_time == 0
        CheckOut.total_waiting_time += now - self.queue.dequeue()
        self.waiting_time = randint(1, CheckOut.nb_checkouts)

    def update(self):
        self.waiting_time = max(0, self.waiting_time - 1)

    def is_free(self):
        return self.waiting_time == 0


for _ in range(20):
    c = CheckOut(Queue())
    c.queue.enqueue(now)

n = 100_000
for _ in range(n):
    now += 1
    c = CheckOut.least_queued_checkout()
    c.queue.enqueue(now)
    for c in CheckOut.checkouts:
        c.update()
        if c.is_free() and not c.queue.is_empty():
            c.serve()

r = sum(len(c.queue) for c in CheckOut.checkouts)
print(CheckOut.total_waiting_time / (n-r))
