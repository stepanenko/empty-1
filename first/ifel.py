name = " "

if not name.strip():
    print("Name is empty")

age = None

if not age:
    print("Provide an age")
elif 18 <= age < 65:
    print("Eligible")
else:
    print("Not eligible")
