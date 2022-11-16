def start_game():
    print("Welcome to the Mission!")
    print("You are a high-level secret agent who is in possession of the Jewel of Medusa")
    diamond = open("jewel.txt", 'r')
    print(diamond.read())
    diamond.close()
    print("Your mission, should you choose to accept, is to get to the airport safely with the jewel")
    choice = input("Press 1 to travel by sea, and 2 to travel by road")
    if choice == "1":
        by_water()
    elif choice == "2":
        by_road()
    else:
        print("\nChoose 1 or 2!")
        start_game()

def game_over(reason):

    print(f"You were {reason}")
    print("GAME OVER!!")
    lose = open("bomb.txt", 'r')
    print(lose.read())
    lose.close()
    play_again()

def play_again():
    print("\nDo you want to play again? Y/N?")
    answer = input(">:").lower()

    if answer == "y":
        start_game()
    elif answer == "n":
        print("\nThanks for playing!")
        exit()
    else:
        print("\nIncorrect input, please type Y or N!")


def win():
    print("\nGreat Job!!! You Did It!!")
    print("Here is your medal...")
    winner = open("win.txt",'r')
    print(winner.read())
    winner.close()
    play_again()

def by_water():
    print("\nWelcome to YOUR MISSION!")
    print("\nYou have decided to take the route by water")
    print("\nIn order to win you must succeed in reaching the airport with the Jewel of Medusa.")
    print("Choose incorrectly and you will fail your mission")
    print("\nYou must choose between the sailboat or jet parked in the water.")
    print("\nSailboat")
    print("Jetboat")
    choice = input("1: Sailboat, 2: Jetboat")

    if choice == "1":
        sail()
    elif choice == "2":
        jet()
    else:
        print("\nChoose 1 or 2!")
        start_game()

def by_road():
    print("\nWelcome to YOUR MISSION!")
    print("\nYou have decided to take the route by road")
    print("\nIn order to win you must succeed in reaching the airport with your jewel")
    print("Choose incorrectly and you will fail your mission")
    print("\nYou've reached a crossroad, one road leads to the police, the other to a deadly gang. Who will you "
          "face?")
    print("\nCops")
    print("Gangsters")

    choice = input("1: Cops, 2: Gangsters")

    if choice == "1":
        cops()
    elif choice == "2":
        gang()
    else:
        print("\nChoose 1 or 2!")
        start_game()

def cops():
    print("\nYou've been caught by the authorities!! They were too smart for you!")
    cop = open("cop.txt",'r')
    print(cop.read())
    cop.close()
    game_over("caught by the cops!")

def gang():
    print("\nThey are a group of three. You can choose to fight them bare-handedly, or shoot them with your gun")
    gangster = open("gang.txt",'r')
    print(gangster.read())
    gangster.close()
    print("Choose now! Fight or Shoot")
    print("\nPress 1 to Fight")
    print("Press 2 to Shoot")

    choice2 = input("Press 1 to Fight or 2 to Shoot")

    if choice2 == "1":
        fight()
    elif choice2 == "2":
        shoot()
    else:
        print("\nJust enter 1 or 2!")
        shoot()

def fight():
    print("\nThere were too many to fight solo. Your mission failed!")
    game_over("beat up by the gangsters")


def shoot():
    shoot = open("gun.txt", 'r')
    print(shoot.read())
    shoot.close()
    print("\nNice! You picked up your gun superfast and shot all three dead.")
    print("Use their horse to ride to the airport not far from here")
    print("\nTerminal 1")
    print("Terminal 2")
    print("")
    choice3 = input("Now choose your terminal. Enter 1 or 2: ")

    if choice3 == "1":
        terminal1()
    elif choice3 == "2":
        terminal2()
    else:
        print("\nStill don't get how to type huh?")
        print("Just enter 1 or 2")

def terminal1():
    print("\nOh no!")
    game_over("caught by border control!")


def terminal2():
    print("\nYOU DID IT!!")
    print("Safely boarding the private jet")
    print("\nMission Complete!!")
    win()



def sail():
    print("\nYou've run out of time!!")
    print("You have failed your mission!")
    print("")
    game_over("out of time")


def jet():
    print("\nCongratulations, you've picked well")
    print("It is the fastest way to reach the airport")
    print("\nTwo ports ahead of you. One crosses pirates, the other the coast security. Choose carefully:")
    print("\n1 for pirates")
    print("2 for coast security")
    choice5 = input("1 or 2: ")

    if choice5 == "1":
        pirates()
    elif choice5 == "2":
        coastguard()
    else:
        print("\nIs it really that hard to type 1 or 2!?")
        choice5 = input("1 or 2")

def pirates():
    print("\nBad luck, the pirates rob your jewel.")
    print("You were left to feed the sharks!")
    sharks = open("shark.txt", 'r')
    print(sharks.read())
    sharks.close()
    game_over("eaten by sharks")


def coastguard():
    print("\nYou have an insider helping you")
    print("You were frisked, but they found nothing")
    print("All you need to do now, is checkin for your flight. Type 'checkin'")
    print("\ncheckin")
    print("")
    prize = input("Enter the action here: ")

    if prize.lower() == "checkin":
        win()
    else:
        print("\nOh you typed it incorrectly and have failed your mission!")
        game_over("unable to checkin on time. You failed!")

start_game()