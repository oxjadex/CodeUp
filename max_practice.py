def max_function(n, max_value):
    if not n:
        return max_value
    current = n.pop()
    if current > max_value:
        max_value = current
    return (max_function(n, max_value))


max_value = 0
n = list(map(int, input().split()))
print(max_function(n, max_value))
