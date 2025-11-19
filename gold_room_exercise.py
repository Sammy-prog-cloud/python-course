from sys import exit


def gold_room():
    print("This room is full of gold. How much do you take? ")
    choice = int(input("> "))
    if 0 in choice or 1 in choice:
        print(f"you chose {choice}")
    else:
        dead("Man learn to type a number")
    if choice < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here")
    print("------------------------------------------")
    print("The bear has a bunch of honey")
    print("------------------------------------------")
    print("The fat bear is in front of another door")
    print("------------------------------------------")
    print("How are you going to move the bear? ")
    print("------------------------------------------")
    print("""
            take honey
            taunt bear
            open door
                        """)
    bear_moved = False
    while True:
        select_choice = input("> ").lower()
        if select_choice == "take honey":
            dead("The bear looks at you then slaps your face off")
        elif select_choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door")
            print("You can go through it now")
            bear_moved = True
        elif select_choice == "Open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in a dark room")
    print("There's a door to your right and left")
    print("Which one do you take? ")
    start_choice = input("> ").lower()
    if start_choice == "left":
        bear_room()
    elif start_choice == "right":
        gold_room()
    else:
        dead("You stumble around the room until you starve")


start()
