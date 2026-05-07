import random

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!','@','#','$','&']

small_letters_length = int(input("How many small letters you want in you password : "))
capital_letters_length = int(input("How many captial letters you want in you password : ")) 
digits_lenth  = int(input("How many digits you want in you password : "))
symbols_lenth = int(input("How many symbols you want in you password : "))

password_list = []

# Getting random small letters
for i in range(0, small_letters_length):
    password_list.append(random.choice(small_letters))

# Getting random capital letters
for i in range(0, capital_letters_length):
     password_list.append(random.choice(capital_letters))

# Getting random symbols
for i in range(0, symbols_lenth):
    password_list.append(random.choice(symbols))

# Getting random digits
for i in range(0, digits_lenth):
    password_list.append(random.choice(digits))
    
print(password_list)

random.shuffle(password_list)

password = ''

for i in password_list:
    password += str(i)
    
print(password)