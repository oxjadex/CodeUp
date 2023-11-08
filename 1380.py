n = int(input())
cnt = 0
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for i in money:
    cnt += n//i
    n = n % i
print(cnt)
