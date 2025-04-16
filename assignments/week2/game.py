import time
import random

def pause():
    time.sleep(1)

print("Welcome to the Mini Basketball Game!")
pause()

name = input("What's your name? ")
pause()

color = input("What color is your jersey? ")
pause()

print(f"Alright {name}, in your {color} jersey — let's get started!")
pause()

action = input("Do you want to SHOOT or PASS? ").lower()
pause()

if action == "shoot":
    print("Okay, you're going for the shot.")
    pause()

    while True:
        try:
            distance = int(input("From how far? 1 (close), 2 (medium), 3 (far): "))
            if distance in [1, 2, 3]:
                break
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")
    pause()

    if distance == 1:
        chance = 90
    elif distance == 2:
        chance = 60
    elif distance == 3:
        chance = 30

    shot = random.randint(1, 100)
    if shot <= chance:
        print("Score! You made the basket!")
        pause()
        if distance == 3:
            print("WOW! A three-pointer! Bonus point for you!")
    else:
        print("Missed the shot!")

elif action == "pass":
    print("You safely passed the ball to your teammate.")
    pause()
else:
    print("You hesitated and lost the ball.")
    pause()

again = input("Do you want to play again? (yes/no) ").lower()
pause()

if again == "yes":
    print("Restarting the game... (but this version ends here)")
elif again == "no":
    print("Okay, see you next time!")
else:
    print("Invalid input, ending the game.")

print("Thanks for playing!")
