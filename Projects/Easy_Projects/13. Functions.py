#Functions

def add(a,b):
    sum = a + b
    print(sum)
    
add(2,3)

def adding(c,d):
    return c+d

sum = adding(3,4)
print(sum)

# Differe between print and return 
"""Return Statement                                         Print Statement
It is used to exit a function and return a value         It is used to display output to the console
It returns a value that can be assigned to a variable    It displays output to the console but does
or used in any expression                                not return the value"""

# 1 Wap to define a function to find square of user input number
def square(a):
    return a**2

a = int(input("Enter number:"))
b = square(a)
print(b)


# 2. WAP to define a function to print name of a student
def name(a):
    return a

a = input("Enter name:")
b = name(a)
print(b)


# 3. Wap to append the value in a list
def change_list(list1):
    list1.append(20)
    list1.append(30)
    return list1

list1 = [10,30,40,50]
b= change_list(list1)
print(b)


# 4. 
def check_age(name, age):
    if age <= 18:
        print(f"Hey {name} can't have this beer")
    else:
        print(f"Hey {name} you get beer.")
    
name = input("Enter name:")
age = int(input("Enter age:"))

check_age(name,age)
check_age(name = "Nitesh",age = 18)
check_age(age = 18, name = "nitesdh")
        