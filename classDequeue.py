class Deque:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.list = [None] *self.capacity

    def isFull(self):
        return self.front == self.capacity-1 or self.rear == 0

    def isEmpty(self):
        return self.rear == self.capacity and self.front == -1

    def AddFront(self, item):
        if self.isFull():
            return print("IndexError: Dequeue is full")
        self.front += 1
        self.list[self.front] = item

    def DeletFront(self):
        if self.isEmpty():
            return print("IndexError: Dequeue is empty")
        self.front -= 1
        self.list[self.front] = None

    def GetFront(self):
        return self.list(self.front)

    def AddRear(self, item):
        if self.isFull():
            return print("IndexError: Dequeue is full")
        self.rear += 1
        self.list[self.rear] = item
        print(self.list[self.rear])

    def DeletRear(self):
        if self.isEmpty():
            return print("IndexError: Dequeue is empty")
        self.rear += 1
        self.list[self.rear] = None 

    def GetRear(self):
        return print(self.list[self.rear])


deque = Deque()

deque.AddFront(1)
deque.AddRear(2)
deque.AddRear(3)

print(deque.isEmpty())  # 출력: False

print(deque.DeletFront())  # 출력: 3
print(deque.DeletRear())  # 출력: 1

print(deque.isEmpty())  # 출력: False
