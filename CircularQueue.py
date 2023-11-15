Queue_Size = 5
list = [None]*Queue_Size
front = 0
rear = 0


def is_Empty():
    return front == rear


def is_Full():
    return (rear+1) % Queue_Size == front


def Enqueue(e):
    global rear, front
    if is_Full():
        return print("Queue is Full")
    rear = (rear+1) % Queue_Size
    list[rear] = e
    return


def Dequeue():
    global rear, front
    if is_Empty():
        return print("Queue is Empty")
    list[(front+1) % Queue_Size] = None
    return


Enqueue(1)
print(list)
Enqueue(2)
print(list)
Enqueue(3)
print(list)
Enqueue(4)
print(list)
Enqueue(5)
print(list)
Dequeue()
print(list)
Enqueue(6)
print(list)