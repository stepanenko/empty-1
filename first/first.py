
print("hello python")
x = 5  # immutable
print(id(x))
x = x + 1  # python will allocate a new memory id for x
print(id(x))

li = [1, 2, 3]  # mutable
print(id(li))
li.append(4)
print(id(li))  # python will use same memory id
