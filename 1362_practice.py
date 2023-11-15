n = int(input())
cnt = 0
for i in range(1, n+1):
    cnt += i
for i in range(n):
    for j in range(i+1):
        print(cnt, end=' ')
        cnt += -1
    print()
