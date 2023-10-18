def max(n, lst):
    if n == 1:
        return lst[0]
    max_n = max(n-1, lst)
    if max_n > lst[n-1]:
        return max_n
    else:
        return lst[n-1]


lst = list(map(int, input().split()))
print(max(len(lst), lst))
