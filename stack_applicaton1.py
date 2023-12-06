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
    if op == '(' or op==')': return 0 #우선 순위가 0 이다
    elif op == '+' or op=='-': return 1 #우선 순위가 1 이다
    elif op == '*' or op=='/': return 2 #우선 순위가 2 이다
    else: return -1
# 부등호 연산자 시험에 나온다

# 중위 표기 -> 후위 표기로 바꾸는 함수
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
        elif term in '+-*/': # + - * / 중에 하나라면
            while not s.isEmpty():
                op= s.peek() # op를 보기만 하기
                if precedence(op) >=precedence(term):
                    output.append(op) # 우선 순위가 더 높다면 output에 넣기 
                    s.pop() #없애기
                else: break
            s.push(term) # stack에 넣기
        else:
            output.append(term) # 그냥 피연산자이면 output에 넣기
        while not s.isEmpty():
            output.append(s.pop()) # stack이 안 비었으면 output에 stack에 넣기

        return output