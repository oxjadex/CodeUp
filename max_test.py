max_value = 0


def maax(n, max_value):
    if not n:
        return max_value
    else:
        current = n.pop()
        if current > max_value:
            max_value = current
        return (maax(n, max_value))


n = list(map(int, input().split()))
print(maax(n, max_value))
