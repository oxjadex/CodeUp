

def ssmm(n, cnt):
    if not n:
        return cnt
    else:
        cnt += n.pop()
        return ssmm(n, cnt)


cnt = 0

n = list(map(int, input().split()))
print(ssmm(n, cnt))
