a, b = map(int, input().split( ))
cnt=0
c=0
arr=list(map(int, input().split( )))
arr.sort()
for i in arr:
    if (cnt%b==0 and i!=0):
        print("\ni")
    print(i,end=' ')
    cnt+=1
