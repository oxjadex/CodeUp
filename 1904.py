def f(a, b):
    if a % 2 == 1:
        print(a, end=' ')
    if a < b:
        f(a+1, b)


a, b = map(int, input().split())
f(a, b)
 