stack_size = 5
list = [None]*stack_size
top = -1


def isEmpty():
    return top == -1


def isFull():
    return top == stack_size-1


def push(e):
    global top
    if not isFull():
        top += 1
        list[top] = e


def pop():
    global top
    if not isEmpty():
        popped_element = list[top]
        list[top] = None
        top -= 1
        return popped_element


def peek():
    if not isEmpty():
        return list[top]


push(1)
push(2)
push(3)
pop()
push(4)
peek()

print(list)
