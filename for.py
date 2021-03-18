
guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
else:  # only runs if while is successful and no break occured
    print("You won")
