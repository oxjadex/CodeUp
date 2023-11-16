class MyStack:
    top = -1
    stack_size = 5
    def __init__(self):
        self._items = []

    def isFull(self, top):
        return top == stack_size-1
    
    def isEmpty(self, top):
        return top == -1
