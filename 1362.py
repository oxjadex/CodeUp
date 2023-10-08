a = int(input())
cnt = 0
for i in range(1, a+1):
    cnt += i
for i in range(a):
    for j in range(i+1):
        print(cnt, end=' ')
        cnt -= 1
    print()

