class Deque:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.list = [None] * capacity

    def isFull(self, capacity):
        return len(self.list) == capacity

    def isEmpty(self):
        return not bool(self.list)

    def AddFront(self, item):
        if self.isFull():
            return print("IndexError: Dequeue is full")
        self.front = item

    def DeletFront(self):
        if self.isEmpty():
            return print("IndexError: Dequeue is empty")
        return self.front == None

    def GetFront(self):
        return print(self.front)

    def AddRear(self, item):
        if self.isFull():
            return print("IndexError: Dequeue is full")
        self.rear = item

    def DeletRear(self):
        if self.isEmpty():
            return print("IndexError: Dequeue is empty")
        return self.rear == None

    def GetRear(self):
        return print(self.rear)


deque = Deque()

deque.AddFront(1)
deque.AddRear(2)
deque.AddRear(3)

print(deque.isEmpty())  # 출력: False

print(deque.DeletFront())  # 출력: 3
print(deque.DeletRear())  # 출력: 1

print(deque.isEmpty())  # 출력: False
