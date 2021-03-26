
def multiply(*values):  # asterisk will convert the 'values' to tuple
    total = 1
    for value in values:
        total *= value
    return total


print(multiply(1, 2, 3, 4))
# 24


def get_user(**user):  # two asterisks will convert the 'user' to dictionary
    print(user)
    print(user["id"])
    print(user["name"])


get_user(id=1, name="John")
# {'id': 1, 'name': 'Jon'} - dictionary, (object in JS)
# 1
# John
