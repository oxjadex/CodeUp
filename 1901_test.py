def f(n):
    if not n:
        return
    print(n.pop(), end=" ")
    return f(n)


n = list(map(int, input().split()))
f(n)
