import random

user = int(input("Enter Positive Int: "))

while user < 1:
    user = int(input("Enter Positive Int: "))

num = random.randint(1,user)

guess = -1

while guess != num:
    guess = int(input("Guess: "))

    while guess < 1:
        guess = int(input("Guess: "))

    if guess == num:
        break
      
    if guess < num:
        print("Too Small!")
    else:
        print("Too Big")
print("Just right")
