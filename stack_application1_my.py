class MyStack:
    top = -1
    stack_size = 100
    list = [None]*stack_size

    def __init__(self):
        self.items = []

    def isFull(self):
        return self.top == self.stack_size-1

    def isEmpty(self):
        return self.top == -1

    def push(self, item):
        if self.isFull():
            return print("스텍이 차있습니다")
        self.top += 1
        self.list[self.top] = item

    def pop(self):
        if self.isEmpty():
            return print("스텍이 비어있습니다")
        self.list[self.top] = None
        self.top -= 1

    def peek(self):
        if not self.isEmpty():
            return print(self.list[self.top])
        else:
            pass

mystack = MyStack()
cnt=0
list=(input())
for i in range (len(list)):
    if 1<= list[i] <=9:
        print(list[i])
    else:
        if list[i]=='*': cnt+=1
        if cnt>=1 and list[i] != '*':
            for i in range(mystack.top):
                mystack.pop()
        else: mystack.push(list[i])

for i in range (mystack.top-1):
    mystack.pop()

def Infix2Postfix(): # *이 나왔을 때 우선 순위 

def precedence(op): # 괄호가 나왔을 때 우선 순위 
    if op == '(':
        return 0 
