"""
# 1. Arithmetic Product and Conditional Logic
# WAP that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
# Case 1: number1 = 20, number2 = 30
# Case 2: number1 = 40, number2 = 30

number1 = int(input("Enter first number:"))
number2 = int(input("Enter seconf number:"))
product = number1*number2
sum = number1+number2
if product <= 1000:
    print(f"The result is {product}")
else:
    print(f"The result is {sum}")

print("*"*50)
#****************************************************************************************************

# 2. Cumulative Sum of a Range
# WAP to Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.
previous_number = 0
sum = 0
for i in range(10):
    sum = i + previous_number
    print(f"Current number is {i} and Previous number is {previous_number} and Sum is {sum}")
    
    previous_number = i

print("*"*50)
#****************************************************************************************************

# 3. String Indexing and Even Slicing
# WAP to Display only those characters which are present at an even index number in given string.
word = "pynative"

even_char = word[0::2]
for i in even_char:
    print(i)

# or

size =  len(word)
for i in range(0, size - 1, 2):
    print("index[",i,"]", word[i])

print("*"*50)
#****************************************************************************************************

# 4. String Slicing and Substring Removal
# Write a function to remove characters from a string starting from index 0 up to n and return a new string.

# remove_chars("pynative", 4)
# remove_chars("pynative", 2)


def remove_char(word,n):
    return word[n:]

print(remove_char("pynative",4))
print(remove_char("pynative",2))

print("*"*50)
#****************************************************************************************************

# 5. WAP to swap the values of two variables, a and b, without using a third temporary variable.
a = 5
b = 10

a, b = b, a
print("a:",a)
print("b:",b)
print("*"*50)
#****************************************************************************************************

# 6. Calculating Factorial with a Loop
# WAP that calculates the factorial of a given number (e.g., 5!) using a for loop.
number = 5
mul = 1
for i in range(1,number+1):
    mul = i * mul
print(mul)
print("*"*50)
#****************************************************************************************************

# 7. List Manipulation: Add and Remove
# Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruits.append("orange")
print(fruits)

fruits.pop(1)
print(fruits)
print("*"*50)
#****************************************************************************************************

# 8. String Reversal
# WAP that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).
text = "Python"

print(text[::-1])
print("*"*50)
#****************************************************************************************************

# 9. Vowel Frequency Counter
# WAP to count the total number of vowels (a, e, i, o, u) present in a given sentence.
sentence = "Learning Python is fun!"
vowels = ['a','e','i','o','u']
count = 0
for i in sentence:
    if i in vowels:
        count += 1
print(count)
print("*"*50)
#****************************************************************************************************

# 10. Finding Extremes (Min/Max) in a List
# Given a list of integers, find and print both the largest and the smallest numbers.
nums = [45, 2, 89, 12, 7]

print("Largest :", max(nums))
print("Smallest :", min(nums))
print("*"*50)
#****************************************************************************************************

# 11. Removing Duplicates from a List
# WAP that takes a list containing duplicate items and returns a new list with only unique elements.
data = [1, 2, 2, 3, 4, 4, 4, 5]

unique_date = list(set(data))
print(unique_date)
print("*"*50)
#****************************************************************************************************

# 12. List Comparison and Boolean Logic
# Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

def comapre(number_list):
    for i in numbers_x:
        if i == numbers_x[-1]:
            return True
        else :
            return False
numbers_x = [10, 20, 30, 40, 10]
print(comapre(numbers_x))

numbers_x = [75, 65, 35, 75, 30]
print(comapre(numbers_x))
print("*"*50)
#****************************************************************************************************

# 13. Filtering Lists with Conditional Logic
#  Iterate through a given list of numbers and print only those numbers which are divisible by 5.
num_list = [10, 20, 33, 46, 55]
for i in num_list:
    if i % 5 == 0:    
        print(i)
print("*"*50)
#****************************************************************************************************

# 14. Substring Frequency Analysis
# WAP to find how many times the substring “Emma” appears in a given string.
str_x = "Emma is good developer. Emma is a writer"
l1 = str_x.split()
for i in l1:
    if i == "Emma":
       c =  l1.count(i)
print(c)
print("*"*50)
#****************************************************************************************************

# 15. Nested Loops for Pattern
# Print the following pattern where each row contains a number repeated a specific number of times based on its value.
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# without nested loop
for i in range(1,6):
    print(f"{i}"*i)

# with nested loop
for i in range(1,6):
    for j in range(i):
        print(i, end= "")
    print("\n")
print("*"*50)
#****************************************************************************************************

# 16. Numerical Palindrome Check
# WAP to check if a given number is a palindrome (reads the same forwards and backwards).
def palindrom(n):
    if n[::] == n[::-1]:
        print(f"True {n} is palindrome")
    else:
        print(False)
palindrom("121")
print("*"*50)
#****************************************************************************************************

# 17. Merging Lists with Parity Filtering
# Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 =[]
for i in list1:
     if i % 2 != 0:
         list3.append(i)
         
for j in list2:
    if j % 2 == 0:
        list3.append(j)
print(list3)
print("*"*50)
#****************************************************************************************************

# 18. Integer Digit Extraction and Reversal
# WAP to each digit from an integer in the reverse order.
number = 7536

while number > 0:
    digit = number % 10 
    number = number // 10
    print(digit, end=" ")

print("*"*50)
#****************************************************************************************************
"""

# 19. Multi-Tiered Income Tax Calculation
