class stack:
    def __init__(self):
        self.stack_size = 5
        self.list = [None]*self.stack_size
        self.top = -1
        self.data = 0

    def isEmpty(self):
        if (self.top == -1):
            return 1
            printf("비었습니다")
        else:
            return 0

    def isFull(self):
        return self.top == self.stack_size-1

    def push(self, e):
        if stack.isFull(self):
            return print("FULL")
        self.top += 1
        self.list[self.top] = e

    def pop(self):
        if stack.isEmpty(self):
            return print("EMPTY")
        popped = self.list[self.top]
        self.list[self.top] = None
        self.top -= 1
        return popped

    def peek(self):
        if not stack.isEmpty(self):
            return print(self.list[self.top])
        else:
            pass

    def print_stack(self):
        return print("현재 stack안의 데이터는 {} 입니다.".format(self.list))


st = stack()

while 1:
    menu = int(input("push(1), pop(2), peek(3), print(4), (5), (6), exit(0): "))
    if menu == 1:
        st.data = int(input("넣을 값을 입력하시오: "))
        st.push(st.data)
    elif menu == 2:
        st.pop()
    elif menu == 3:
        st.peek()
    elif menu == 4:
        st.print_stack()
    elif menu == 5:
        st = 0
    elif menu == 6:
        st = 0
    else:
        break
