age = int(input("Please enter your age: "))

if age >= 18 and age < 60:
    print("You are old enough to purchase alcohol.")
    
elif age >= 60:
    print("You are old enough to purchase alcohol, but please drink responsibly.")

else:    
    print("You are not old enough to purchase alcohol.")