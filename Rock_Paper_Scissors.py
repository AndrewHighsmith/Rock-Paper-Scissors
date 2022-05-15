from operator import truediv
import random

user_wins = 0
computer_wins = 0


options = ["rock", "paper", "scissors"]

running = True

while running == True:
    user_input = str(input("Type Rock/Paper/Sissors or Q to quit: ")).lower()
    if user_input == "q":
        running = False

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #Rock: 0, Paper: 1, Scissors: 2
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!!!")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick == "rock":
        print ("You Won!!!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print ("You Won!!!")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("You tied!")
    
    elif user_input == "paper" and computer_pick == "paper":
        print("You tied!")
    
    elif user_input == "scissors" and computer_pick == "scissors":
        print("You tied!")
    
    else:
        print("You Lost!")
        computer_wins += 1
    

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye")
