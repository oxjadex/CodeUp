stack_size = 5
list = [None]*stack_size
top = -1


def isEmpty():
    global top
    if top == -1:
        return True
    return False


def isFull():
    global top
    if top == stack_size-1:
        return True
    return False


def push(e):
    global top
    if isFull():
        return print("스텍이 꽉 차있습니다.")
    top += 1
    list[top] = e


def pop():
    global top
    if isEmpty():
        return print("스텍이 비어있습니다.")
    popped = list[top]
    list[top] = None
    top -= 1
    return popped


def peek():
    global top
    if not isEmpty():
        return print(list[top])
    else:
        pass


push(1)
push(2)
push(3)
push(4)
push(5)
pop()
pop()
pop()
peek()

print(list)