queue_size = 5
list = [None]*queue_size
front = 0
rear = 0

def isFull():
    return (rear+1) % queue_size == front

def isEmpty():
    return front == rear

def enqueue(data):
    global rear
    if not isFull():
        rear = (rear + 1) % queue_size
        list[rear] = data
    else:
        print("가득참")

def dequeue():
    global front
    if not isEmpty():
        front = (front + 1) % queue_size
        data = list[front]
        return data
    else:
        print("비었음")

def peek():
    if(isEmpty()):
        print("비었음")
    else:
        return list[(front+1) % queue_size]

enqueue(3)
print(list)
enqueue(4)
print(list)

enqueue(5)
print(list)

enqueue(6)
print(list)

enqueue(7)
print(list)

print(dequeue())

enqueue(8)
print(list)
