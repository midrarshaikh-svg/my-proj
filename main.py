import random
randomNum = random.randint(1,100)
print(randomNum)

while True:
    userguess = int(input("Guess a correct number: "))
    if userguess == randomNum:
        print("Success: You guessed the correct integer!!")
        break
    elif userguess < randomNum:
        print("Your guess was too cheap, take a higher integer next time")
    else:
        print("your guess was too high, take a cheapest integer next time")
        print("-----Game Over-----")

