a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)
s = a
for i in range(2, n+1):
    s *= r

print(s)
