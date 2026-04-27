# A game in which computer and user will play rock paper scissor game and computer will choose 
# randomly and user will input his choice and then we will decide who is the winner

import random
print("Welcome to Rock Paper Scissor Game!")
print("Enter your choice: ")
print("1. Rock")
print("2. Paper")
print("3. Scissor")
user_choice = int(input("Your choice from  1, 2, or 3: "))
choices = ["Rock", "Paper", "Scissor"]
computer_choice = random.choice(choices)
print(f"Computer chose: {computer_choice}")

if user_choice == 1:
    if computer_choice == "Rock":
        print("It's a tie!")
    elif computer_choice == "Paper":
        print("Computer wins!")
    else:
        print("You win!")

elif user_choice == 2:
    if computer_choice == "Rock":
        print("You win!")
    elif computer_choice == "Paper":
        print("It's a tie!")
    else:
        print("Computer wins!")

elif user_choice == 3:
    if computer_choice == "Rock":
        print("Computer wins!")
    elif computer_choice == "Paper":
        print("You win!")
    else:
        print("It's a tie!")
else:
    print("Invalid choice! Please choose 1, 2, or 3.")

