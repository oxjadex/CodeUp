a = list(input())
cnt = 0
while cnt != 0 or cnt < 10:
    for i in range(len(a)):
        cnt += int(a[i])
    a = list(map(int, str(cnt)))

print(cnt)
