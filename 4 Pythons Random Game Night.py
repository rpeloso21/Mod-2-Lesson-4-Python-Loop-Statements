# Task 1
import random

dice_outcomes = []

for x in range(1, 13):
    dice_outcomes.append(x)

input("Welcome to our casino!  Would you like to play a game of dice?")

print("Excellent, I knew you were a betting sort.")

guess = 1

while True:
    try:
        guess = int(input("Please select a numbe from 1 to 12: "))
    except:
        print("I'm sorry.  That was not a valid guess.  Please try again.")
        continue
    
    if (type(guess) == int) and (0 < guess < 13):
        print("Excellent choice my friend!")
        break
    else:
        print("I'm sorry.  That was not a valid guess.  Please try again.")
        

print("Now, lets see how you have done...")
roll = random.choice(dice_outcomes)
print(f"and the role is ......... {roll}!!!!")

if int(guess) == int(roll):
    print(f"Congratulation my friend. It looks like {guess} is your lucky number. You have won $1,000,000!!!")

else:
    print("Not so lucky this time. Maybe try again later.")

