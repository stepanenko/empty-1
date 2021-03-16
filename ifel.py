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

age = 19
# Ternary:
message = "Eligible" if 18 <= age < 65 else "Not eligible"
print(message)
