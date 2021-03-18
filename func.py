# def = define or function definition
def increment(num, by=1):  # 'by' now has 1 as a default value
    return (num, num * by)


# also valid, with type annotations
# after -> we put returned type, here its 'tuple'
def increment2(num: int, by: int = 1) -> tuple:
    return (num, num * by)


# res = increment(num=5, by=4) - also valid, called keyword arguments
res = increment(num=5, by=4)
print(res)

res2 = increment2(13)
print(res2)


print((1, 2, 3))  # will print TUPLE (read only list) - (1, 2, 3)
[4, 5, 6]  # list
(1, 2, 3)  # tuple
