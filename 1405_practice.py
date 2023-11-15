n = int(input())
k = list(map(int, input().split()))
for i in range(n):
    print(*k)
    k.append(k.pop(0))
