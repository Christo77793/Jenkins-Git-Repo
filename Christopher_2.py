import time

print("Welcome to the text based adventure game!!!")

health = 100

# BLUE DOOR VARIABLES

choice = ""
time_count = 0
bullet_count = 3
deep_search = 0
item_search = ""

answer = input("\nDo you want to start playing (yes/no): ").lower()
if answer == "yes":
    print("\nAlright let's begin")

    print(f"\nYour health is {health}")
    print('''\nYou wake up in a void with no idea or memories of the events that led to this. Baffled as you are then you see
3 doors fades in ahead of you. One colored blue another colored green and the last one colored red. Nothing is there behind
and besides the 3 doors and you decide to open 1 door''')

    # DOOR SELECTION

    door = input("\nChoose a door (input either blue, green or red): ").lower()
    if door == "blue":

        # BLUE DOOR

        print('''\nThings get even weirder because now that you opened the blue door you are suddenly in a room. You 
wonder what just happened and try to make sense of it''')
        while choice != "e":

            # THINK OR ESCAPE

            choice = input("\nKeep thinking about it or try to escape (input t to think and e to escape): ").lower()
            if choice == "t":
                print("You keep thinking about it")
                if time_count == 1:
                    print("Stop wasting time")
                elif time_count > 1:
                    print('''You hear a strange bubbly sound from above and you look up to see vat of acid burning through the roof and
a drop of acid falls on you which burns you and you lose health (-10)''')
                    health -= 10
                    print(f"Your health is {health}")
                    if health <= 0:
                        print("Your health is 0")
                        print("You lost!!!")
                        exit()
                    print("{press e to continue and not loose further health}{or go crazy and loose all your health}")
            time_count += 1
        print(f"\nYour health is {health}")
        print("With no thoughtful conclusions you decide to try and escape ")
        print("You look around for items and supplies that you could use")
        print("You see a medi-kit, a sword, a pistol with 3 bullets, and a gas mask")

        # INVENTORY SELECTION

        print("\n###Remember 3rd time's the charm###\n")
        while item_search != "no":
            item_search = input("Do you want to look for more items (yes/no) ? ").lower()
            if deep_search <= 1:
                print("Found nothing ...")
                deep_search += 1
            elif deep_search > 1:
                print("You found 2 more bullets and a map")
                bullet_count += 2
                break
        print("\nWhat all would you like to take with you ? ")
        print("You can take 3 items")
        supply_choice1 = input("Enter the first item: ")
        supply_choice2 = input("Enter the second item: ")
        supply_choice3 = input("Enter the third item: ")
        print(f"You chose {supply_choice1}, {supply_choice2}, and {supply_choice3}")
        if supply_choice1.lower() == "pistol" or supply_choice2.lower() == "pistol" or supply_choice3.lower() == "pistol":
            print(f"You have {bullet_count} bullets for your pistol")

        print('''\nYou got your things now you keep moving on. However after you take a few steps ahead things get even weirder 
again as a door shuts behind you and you are now suddenly in the middle of a forest!''')

        if supply_choice1.lower() == "map" or supply_choice2.lower() == "map" or supply_choice3.lower() == "map":
            print('''\nYou try to re-open the door but it seems to be bolted from the other side. But you are relieved with
your decision to take the map and you decide to put the map good use and keep moving forward''')
            print('''\nYears of learning Geography and now that you have to finally put it to use, you can't remember a damn thing
But however despite everything you notice that the markings on the map does not seem normal''')
            print("\nYou think to yourself 'Ugh what was I expecting nothing has been normal for a while now'")
            print('''You try your best to decode and make sense of the map, but then a loud and ferocious roar, makes you
stand guard. You then hear the roar again but louder and closer as  if it was getting closer towards you and at a fast rate too.''')
            if supply_choice1.lower() == "pistol" or supply_choice2.lower() == "pistol" or supply_choice3.lower() == "pistol":
                print(f"You draw out the pistol and get ready for anything")
            elif supply_choice1.lower() == "sword" or supply_choice2.lower() == "sword" or supply_choice3.lower() == "sword":
                print(f"You draw out the sword and get ready for anything")
            print('''\nThrough the bush ahead of you a huge lion jumps out in front of you. You being the intellectual 😉
can think of only 2 things''')
            map_choice = input("Choose A to Stand your guard and fight or B to run: ").lower()
            if map_choice == "a":
                print('''You think to yourself this is no ordinary lion. It is at least 5 times as huge as a normal lion. Running
felt like a easy option, but only a fool would run. ''')
                print('''A dark ''')
            elif map_choice == "b":
                print("\nYou think to yourself 'Na, I'm not cut out for battle', and you run")
                time.sleep(5)
                print("\n{Here's a tip to whoever is playing this}")
                time.sleep(3)
                print("\nYOU DON'T RUN WHEN YOU ENCOUNTER A WILD ANIMAL! ###facepalm###")
                health = 0
                print(f"Your health is {health}")
                print("YOU ARE DEAD!!!")
                exit()
        else:
            print('''You wish you had taken the map; so you try to open the door but it seems to be bolted from the other side
and now''')
            print('''Without the map you now rely on your wit and instinct and hope these 2 along with a prayer that God be with
you, you move on!''')


elif answer == "no":
    print("That's too bad")
else:
    print("Invalid input!")