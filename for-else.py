
names = ["Lily", "Peter"]

found = False
for name in names:
    if name.startswith("L"):
        print("Found")
        found = True
        break

if not found:
    print("Not found")

# Better solution:
for name in names:
    if name.startswith("L"):
        print("Yes")
        break
else:  # will execute else block if break was not reached and after all items are iterated over
    print("No")

for x in range(1000000):
    if x == -10:
        break
else:  # will execute else block if break was not reached and after all items are iterated over
    print("end")
