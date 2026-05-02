# Print 9 box
# find 1 box with treasure (randomly)
# User have 3 life line to choose treasure box

import random
import sys

row1 = ['A', 'A', 'A']
row2 = ['A', 'A', 'A']
row3 = ['A', 'A', 'A']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

choose = ["11","12","13","21","22","23","31","32","33"]
computer_choice = random.choice(choose)
print(f"The treasure box by computer is {computer_choice}")


# By For Loop
for i in range(1,4):
    user_input = input(f"Enter your {i} number:")
    row = int(user_input[0])-1
    column = int(user_input[1])-1
    print(f"The row : {row} and column : {column} is given by user")
    if computer_choice == user_input:
        print("You Won")
        map[row][column] = "W"
        print(f"{row1}\n{row2}\n{row3}")
        sys.exit()
    else :
        print(f"{i} option is wasted.")
        
    map[row][column] = 'N'
    print(f"{row1}\n{row2}\n{row3}")




# Without Loop

# user_input = input("Enter your first number:")
# row = int(user_input[0])-1
# column = int(user_input[1])-1
# # In python the indexn are start from 0 thats why we use -1 in row and column
# print(f"The row : {row} and column : {column} is given by user")
# if computer_choice == user_input:
#     print("You Won")
#     map[row][column] = "W"
#     print(f"{row1}\n{row2}\n{row3}")
#     sys.exit()
# else :
#     print("First option is wasted again")


# # mapping the user's first choice
# map[row][column] = 'N'
# print(f"{row1}\n{row2}\n{row3}")


# #****************************************Second Option********************************************

# user_input = input("Enter your second number:")
# row = int(user_input[0])-1
# column = int(user_input[1])-1
# # In python the indexn are start from 0 thats why we use -1 in row and column
# print(f"The row : {row} and column : {column} is given by user")
# if computer_choice == user_input:
#     print("You Won")
#     map[row][column] = "W"
#     print(f"{row1}\n{row2}\n{row3}")
#     sys.exit()
# else :
#     print("Second option is wasted again")


# # mapping the user's first choice
# map[row][column] = 'N'
# print(f"{row1}\n{row2}\n{row3}")

    
# #****************************************Third Option ***********************************************    
# user_input = input("Enter your third number:")
# row = int(user_input[0])-1
# column = int(user_input[1])-1
# # In python the indexn are start from 0 thats why we use -1 in row and column
# print(f"The row : {row} and column : {column} is given by user")
# if computer_choice == user_input:
#     print("you Won")
#     map[row][column] = "W"
#     print(f"{row1}\n{row2}\n{row3}")
#     sys.exit()
# else :
#     print("Your all options are wasted you losse the game")


# # mapping the user's first choice
# map[row][column] = 'N'
# print(f"{row1}\n{row2}\n{row3}")
