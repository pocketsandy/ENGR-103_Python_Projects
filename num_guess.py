import random

rand_integer = random.randint(1,100)
num_guess = 0

print("Enter the integer for the player to guess.")

while True:
    guess = int(input("Enter your guess: "))
    num_guess += 1

    if guess > rand_integer:
        print("Too high - try again.")
    elif guess < rand_integer:
        print("Too low - try again.")
    else:
        if num_guess == 1:
            print("You guessed it in 1 try.")
        else:
            print("You guessed it in", num_guess, "tries.")
