name: str = input("Hey type your name: ")
print(f"Hello {name}, welcome to the adventure game!")
print("*********************************************");
print()

play = input("Do you want to play? (yes/no): ").lower()
if play == "yes" or play == "y" or play == "1":
    print("Let's start the game!")
    print("*********************************************");
    # weapon = input(f"Okay {name}, you are on an adventure, choose a weapon (sword/axe): ").lower()
    
    direction = input("You are on a road, which direction do you want to go? (left/right): ").lower()
    if direction == "left" or direction == "l" or direction == '1':
        print(f"{name}, You went left and fell of a cliff ⺁, game over😭, try again!.")
    elif direction == "right" or direction == "r" or direction == '2':
        choice = input(f"Okay {name}, you are now at a lake, do you want to swim or cross the bridge? (swim/cross): ").lower()
        if choice == "swim" or choice == "s" or choice == '1':
            print(f"{name}, You swam and got eaten by a shark 🦈, game over, try again😭!")
        elif choice == "cross" or choice == "c" or choice == '2':
            print(f"{name}, You crossed the bridge and found the gold! you won the game, congratulations🎉!")
        else:
            print(f"{name}, Invalid choice, game over, try again!.")
    else:
        print(f"Invalid input {name}, game over, try again!.")
else:
    print(f"Goodbye {name}!")
    exit()   