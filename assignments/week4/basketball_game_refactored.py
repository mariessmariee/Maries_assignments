import time
import random

# Constants
CLOSE_CHANCE = 90
MEDIUM_CHANCE = 60
FAR_CHANCE = 30
WAIT_TIME = 1


# Helper Functions
def pause():
    time.sleep(WAIT_TIME)


def get_chance(distance):
    # This function returns the chance of scoring based on distance
    if distance == 1:
        return CLOSE_CHANCE
    elif distance == 2:
        return MEDIUM_CHANCE
    elif distance == 3:
        return FAR_CHANCE
    else:
        return 0  # in case of an unexpected value


def play_turn(name, color):
    print(f"Alright {name}, in your {color} jersey — let's get started!")
    pause()

    action = input("Do you want to SHOOT or PASS? ").lower()
    pause()

    if action == "shoot":
        print("You're going for the shot!")
        pause()

        while True:
            try:
                distance = int(input("How far? 1 (close), 2 (medium), 3 (far): "))
                if distance in [1, 2, 3]:
                    break
                else:
                    print("Please choose 1, 2, or 3.")
            except ValueError:
                print("Enter a number, not text.")

        pause()

        chance = get_chance(distance)
        shot = random.randint(1, 100)

        if shot <= chance:
            print("Nice! You scored!")
            if distance == 3:
                print("Three-pointer! Extra cool!")
        else:
            print("Oh no! You missed.")

    elif action == "pass":
        print("Good pass to your teammate!")
    else:
        print("You waited too long and lost the ball.")
    pause()


# Main Function
def main():
    print("Welcome to the Mini Basketball Game!")
    pause()

    name = input("What’s your name? ")
    pause()

    color = input("What color is your jersey? ")
    pause()

    play_turn(name, color)

    again = input("Do you want to play again? (yes/no) ").lower()
    pause()

    if again == "yes":
        print("Let’s restart! (But this version ends here)")
    elif again == "no":
        print("Thanks for playing!")
    else:
        print("Didn't get that — ending the game.")


# Run the game
if __name__ == "__main__":
    main()
