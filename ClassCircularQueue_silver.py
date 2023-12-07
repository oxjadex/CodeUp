class Queue:
    def __init__(self, Queue_Size):
        self.Queue_Size = Queue_Size
        self.list = [None] * Queue_Size
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.Queue_Size == self.front

    def enqueue(self, e):
        if self.isFull():
            return print("큐가 가득 찼습니다.")
        self.rear = (self.rear + 1) % self.Queue_Size
        self.list[self.rear] = e
        return

    def dequeue(self):
        if self.isEmpty():
            return print("큐가 비어있습니다.")
        self.front = (self.front + 1) % self.Queue_Size
        self.list[self.front] = None
        return