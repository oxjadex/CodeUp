class stack():

    def __init__(self):
        self.top=-1
        self.stack_size=5
        self.s_list=[None]*self.stack_size
    

    def isFull(self):
        return self.top == self.stack_size-1
            
    
    def isEmpty(self):
        return self.top==-1 

    def push(self, e):
        if self.isFull(): 
            return print("스택이 가득찼습니다  ")
        self.top+=1
        self.s_list[self.top]=e


    def pop(self):
        if self.isEmpty():
            return print("스택이 비었습니다. ")
        self.top-=1


    def peek(self):
        if not self.isEmpty():
            print(self.s_list[self.top])
        else :
            pass

    

S=stack()
S.push(1)
S.push(2)
S.push(3)
S.peek()
S.pop()
print(S.s_list)

