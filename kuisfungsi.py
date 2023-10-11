def minimal(a, b):
    if a < b:
        return a
    elif a > b:
        return b
    elif a == b:
        return a


result = minimal(50, 50)
print(result)
