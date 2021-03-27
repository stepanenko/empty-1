
def multiply(*values):  # asterisk will convert the 'values' to tuple
    total = 1
    for value in values:
        total *= value
    return total


print("start")  # at this line press F9 to add breakpoint then go to Debug tab
print(multiply(1, 2, 3, 4))
print("end")
