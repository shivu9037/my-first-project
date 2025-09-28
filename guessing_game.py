import random 
number=random.randint(1,100)
print("welcome to my number guessing name")
print("can u guess the nuumber between 1 to 100")
attempts=0
guess=0
while guess!=number:
    guess=int(input("enter your guess:"))
    attempts+=1
    if guess<number:
        print("your guess is too low")
    elif guess>number:
        print("your guess is too high")
    else:
        print("congratutlations you have gussed the number in",attempts,"attempts")
        print("your number is correct that is",number)