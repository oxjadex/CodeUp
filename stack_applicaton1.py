class MyStack:
    top = -1
    stack_size = 5
    list=[None]*stack_size

    def __init__(self, stack_size):
        self.stack_size = stack_size

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

#연산 우선 순위 계산 함수
def precedence(op): 
    if op == '(' or op==')': return 0
    elif op == '+' or op=='-': return 1
    elif op == '*' or op=='/': return 2
    else: return -1
# 부등호 연산자 시험에 나온다
#중위 표기 -> 후위 표기로 바꾸는 함수
def Infix2Postfix(expr):
    s = MyStack(100)
    output=[]
    for term in expr: 
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op=s.pop()
                if op=='(':
                    break
                else: output.append(op)
        elif term in '+-*/':
            while not s.isEmpty():
                op= s.peek()
                if precedence(op) >=precedence(term):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        else:
            output.append(term)
        while not s.isEmpty():
            output.append(s.pop())

        return output