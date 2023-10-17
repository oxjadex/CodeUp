def pr(n):
    if not n:
        return
    else:
        print(n.pop())
        pr(n)


n = list(map(int, input().split()))
pr(n)
