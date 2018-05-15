l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7]))


# print(l)

def is_odd(n):
    return n % 2 == 1


L = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print(L)
