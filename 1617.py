n = int(input())
rn = int(str(n)[::-1])
sum = rn+n
r_sum = int(str(sum)[::-1])
if sum == r_sum:
    print("YES")
else:
    print("NO")
