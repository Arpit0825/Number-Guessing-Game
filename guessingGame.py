import random

a = random.randint(1,9)
chance = 0

print("Guess A Number (between 1-9)")

while chance < 5:
    b = int(input("Enter your guess: "))
    if b==a:
        print("Congratulations YOU WON!!!")
        break
    elif b < a:
        print("Your Guess is too low: Guess a higher number than",b)
    else:
        print("Your Guess is too high: Guess a smaller number than",b)

    chance = chance+1 

if not chance < 5:
    print("You lose, the number is",a)
