class MyStack:
    top = -1
    stack_size = 5
    list=[None]*stack_size

    def __init__(self):
        self.items = []

    def isFull(self):
        return self.top == self.stack_size-1

    def isEmpty(self):
        return self.top == -1

    def push(self, item):
        if self.isFull():
            return print("스텍이 차있습니다")
        self.top+=1
        self.list[self.top]=item

    def pop(self):
        if self.isEmpty():
            return print("스텍이 비어있습니다")
        self.list[self.top]=None
        self.top-=1

    def peek(self):
        if not self.isEmpty():
            return print(self.list[self.top])
        else: pass

    
mystack = MyStack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.push(5)
mystack.pop()
mystack.pop()
mystack.pop()
mystack.peek()

print(mystack.list)