def f(n):
    if len(n) != 1:
        return n.pop() + f(n)
    return n.pop()


n = list(map(int, input().split()))
print(f(n))
