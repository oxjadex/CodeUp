class MyStack:
    top = -1
    stack_size = 5

    def __init__(self):
        self.items = []

    def isFull(self, top):
        return self.top == self.stack_size
    
    def isEmpty(self, top):
        return self.top == -1
