stack_size = 5
list = [None]*stack_size
top = -1


def isEmpty():
    if top == -1:
        return True
    else:
        return False


def isFull():
    return top == stack_size-1


def push(e):
    global top
    if not isFull():
        list.append(e)


def pop():
    if not isEmpty():
        print(list[top])
        list[top] = None
        top -= 1


def peek():
    if not isEmpty():
        print(list[top])
    else:
        pass


push(1)
push(2)
push(3)
pop()
push(4)
peek()

print(list)
