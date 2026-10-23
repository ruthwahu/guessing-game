print("Welcome to the number guessing game !")
import random 
secret = random.randint(1,10)
guess=int(input("Guess a number from 1 to 10: "))
print("you guessed",guess)
if guess ==secret:
    print("you win!")
else:
    print("Nope !The secret number was",secret)