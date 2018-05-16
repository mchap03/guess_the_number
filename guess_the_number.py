import random
guessnum = 0
num = random.randint(1, 100)

print("Guess the number that is in my mind between 1 and 100")



while guessnum < num:
    print("take a guess")
    guess = input()
    guess = int(guess)
    if guess < num:
        print("That's too low and try again")
    if guess > num:
        print("That's too high and try again")
    elif guess == num:
        print("Congrats you nailed it")


