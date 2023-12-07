a = input()
for i in a:
    if 'A'<=i and i<='Z' :
        print(chr(ord(i)+32), end='')
    elif 'a'<=i and i<='z' : print(chr(ord(i)-32), end='')
    else: print(i,end='')

