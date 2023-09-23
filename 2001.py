p_max = 2001
j_max = 2001
for i in range(3):
    a = int(input())
    if a < p_max:
        p_max = a
for i in range(2):
    a = int(input())
    if a < j_max:
        j_max = a
p_max = float(p_max)
sum = p_max+j_max
price = sum+sum//10.0
print('%.1f' % price)
