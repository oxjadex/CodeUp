a = int(input())

b = input().split(' ')

for i in range(a):
    for j in range(a):
        print(b[(i+j) % a], end=(' '))
    print()
