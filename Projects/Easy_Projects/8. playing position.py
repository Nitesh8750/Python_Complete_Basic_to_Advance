# WAP to choose who will play at 1st, 2nd, 3rd, 4th and 5th position
#  players are "Ravi", "Shweta","Mahime","Akshay","Ritik"

import random

player = ["Ravi", "Shweta","Mahime","Akshay","Ritik"]

# selected_player = random.choice(player)

# print(f"First player is {selected_player}")

# player.remove(selected_player)

print(player)

for i in range(1, len(player)+1):
    selected_player = random.choice(player)
    print(f"{i} player is {selected_player}")
    player.remove(selected_player)
    # Only print the list if it's not empty
    if player:
        print(player)
    