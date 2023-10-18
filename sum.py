cnt = 0


def ssmm(n):
    global cnt
    if not n:
        return cnt
    else:
        cnt += n.pop()
        return ssmm(n)


n = list(map(int, input().split()))
print(ssmm(n))
