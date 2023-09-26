k,n =map(int,input().split())
maxi=0
while k>=n:
    k=k-n
    k+=1
    maxi+=1

print(maxi)