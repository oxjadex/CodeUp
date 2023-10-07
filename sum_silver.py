def sumd(n):
    if len(n) != 1:
        return n.pop() + sumd(n)
    return n.pop()


n = list(map(int, input().split()))
print(sumd(n))
