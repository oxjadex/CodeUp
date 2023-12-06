class Queue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise Exception("IndexError: Queue is full")

        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("IndexError: Queue is empty")

        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "IndexError: Queue is empty"

        return self.queue[0]