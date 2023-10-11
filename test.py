def suum(test):
    if not test:
        return 0
    else:
        return int(test.pop()) + suum(test)


test = list(input().split())
print(suum(test))
