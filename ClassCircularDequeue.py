class Queue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.list = [None] *self.capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front

    def Addfront(self, e):
        if self.isFull():
            return print("IndexError: Queue is full")
        self.list[self.rear] = e
        self.front = (self.front - 1) % self.capacity
        return

    def Deletefront(self):
        if self.isEmpty():
            return print("IndexError: Queue is empty")
        self.front = (self.front + 1) % self.capacity
        self.list[self.front] = None
        return