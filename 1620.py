n = int(input())
c=0
while (c==0 or c>=10) :
    c=0
    while (n!=0):
        c+=n %10
        n=n//10
    n=c
print(c)
