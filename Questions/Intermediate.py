# 1. Check if all elements in a list are unique
def unique():
    a = [1,2,3,4,5]
    for i in a:
        if a.count(i) == 1:
            print("unique")
        # return len(a) == len(set(a))
unique()

print("*"*50)
#***************************************************************************************************


# 2. Find the product of all elements in a list
def product():
    a = [1, 2, 3, 4]
    multi = 1
    for i in a:
        multi = multi * i
    # print(multi)
    return multi
print(product())

print("*"*50)
#***************************************************************************************************

# 3. Count the occurrences of each element in a list
def occurance():
    a = [1, 2, 2, 3, 3, 3]
    for i in a:
        b = a.count(i)
        print(f"the count of {i} is {b}")
occurance()

print("*"*50)
#***************************************************************************************************


# 4. Find the sum of the digits of a number until the result has only one digit
def sum(a):
    while int(a) > 10:
        b = 0
        for i in a:
            b = b + int(i)
        print(b)
        break
a = input("Enter digit :")
sum(a)

print("*"*50)
#***************************************************************************************************


# 5. Find the number of words in a sentence
def numberofwords():
    word = "Python programming is fun"
    length = len(word.split())
    print(length)
numberofwords()

print("*"*50)
#***************************************************************************************************


# 6. Find the number of p in a sentence
def numberofdigit():
    word = "Python programming is fun"
    count = 0
    for i in word:
        if i.lower() == 'p':
            count =  count + 1
    print(count)
    # length = len(word.split())
    # print(length)
numberofdigit()

print("*"*50)
#***************************************************************************************************


# 7. Find the second most frequent character in a string
def second_most_frequent():
    word = "success"
    seen = []
    
    first_char = None
    first_count = 0
    
    second_char = None
    second_count = 0
    
    for i in word:
        if i not in seen:
            count = word.count(i)
            seen.append(i)
            
            # Logic to find the top two
            if count > first_count:
                # Old 1st place drops to 2nd place
                second_count = first_count
                second_char = first_char
                # New 1st place
                first_count = count
                first_char = i
            elif count > second_count and count < first_count:
                # New 2nd place
                second_count = count
                second_char = i
                
    print(f"1st Place: '{first_char}' ({first_count} times)")
    print(f"2nd Place: '{second_char}' ({second_count} times)")

second_most_frequent()

print("*"*50)
#***************************************************************************************************


# 8 Check if two lists are identical
# when two list are same
def indentical_list():
    l1 = [1,2,3]
    l2 = [1,2,3]
    return l1 == l2
print(indentical_list())

print("*"*50)
#***************************************************************************************************



# 9 Rotate a matrix 90 degrees clockwise
def rotate_matrix():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Test
    # matrix = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]]     
    
    matrix = list(zip(*matrix[::-1]))
    # 1. [::-1] reverses the order of the rows -->  The [::-1] slice flips the outer list upside down.
    # [
    # [7, 8, 9],  # Was the bottom row
    # [4, 5, 6],
    # [1, 2, 3]   # Was the top row
    # ]
    
    # 2. Adding the asterisk * before matrix[::-1] strips away the outer brackets and feeds the rows into zip() as separate lists.
    # It turns into this: zip([7, 8, 9], [4, 5, 6], [1, 2, 3])
    
    # 3. zip(*) groups the elements into columns 
    # The zip() function takes the first elements of all lists and groups them together, then the second elements, then the third.
    return [list(row) for row in matrix]
    
    # output would be
        # [
        # [7, 4, 1],
        # [8, 5, 2],
        # [9, 6, 3]
        # ]

print(rotate_matrix()) 

print("*"*50)
#***************************************************************************************************



# 10. Remove all spaces from a string
def space(s):
    s.replace(" ","")
    return s
print(space("Hello World"))

print("*"*50)
#***************************************************************************************************


# 11 Capitalize the first letter of each word in a string
def capitalize_first_letter(s):
    # s = "python is fun"
    # b = s.capitalize()
    b = s.title()
    return b
print(capitalize_first_letter("python is fun"))

print("*"*50)
#***************************************************************************************************


# 12 Check if a string is a pangram (contains every letter of the alphabet at least once)
def pangram():
    word = "The quick brown fox jumps over the lazy dog"
    word = word.replace(" ","")
    for i in word:
        if i.isalpha():
            len(set(i.lower())) == 26
    return "This strig is pangram"
print(pangram())

print("*"*50)
#***************************************************************************************************


# 13. Generate a list of prime numbers up to n
def prime_numbers_to_n():
    n = 10
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

print(prime_numbers_to_n())  # Output: [2, 3, 5, 7]
print("*"*50)
#***************************************************************************************************


# 14. Merge two dictionaries
def merg_dictonaries():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    dict1.update(dict2)
    return dict1
print(merg_dictonaries())
print("*"*50)
#***************************************************************************************************


# 15. Find the maximum difference between two consecutive elements in a sorted list
def max_difference():
    l1 = [1, 3, 8, 12, 20]
    l2 = []
    for i in range(1, len(l1)):
        a = l1[i] - l1[i-1]
        l2.append(a)
    return max(l2)
print(max_difference())
print("*"*50)
#***************************************************************************************************


# 16. Find the sum of all elements in a nested list
def sum_nested_list(nested_lst):
    total = 0
    for element in nested_lst:
        if isinstance(element, list):
            total += sum_nested_list(element)
        else:
            total += element
    return total

nested_lst = [[1, 2, [3]], [4, 5]]
print(sum_nested_list(nested_lst))  # Output: 15
print("*"*50)
#***************************************************************************************************


# 17. Reverse the words in a sentence
def reverese_words():
    word = "Python is fun"
    return ''.join(word.split()[:,:,-1])
    
print(reverese_words())
print("*"*50)
#***************************************************************************************************


# 18. Create a list of all odd numbers between two given numbers (inclusive)
def odd_numbers():
    start = 3
    end = 10
    l1 = []
    for i in range(start, end+1):
        if i % 2 != 0:
            l1.append(i)
    return l1
print(odd_numbers()) 
print("*"*50)
#***************************************************************************************************


# 19. Check if a number is an Armstrong number
def armstrong():
    n = 153
    sum = 0
    for i in str(n):
        sum = sum + int(i)**3
        if n == sum:
            print("Number is Armstrong")
armstrong()
print("*"*50)
#***************************************************************************************************



# 20. Find the common divisors of two numbers
def common_divisor():
    a,b = 12, 18
    l1 = []
    for i in range(1, min(a,b)+1):
        if a%i == 0 and b%i == 0:
            l1.append(i)
    return l1

print(common_divisor())
print("*"*50)
#***************************************************************************************************


# 21 Find all palindromic numbers between two given numbers
def palindrome_numbers():
    a,b = 100, 150
    l1=[]
    for i in range(a, b+1):
        if str(i) == str(i)[::-1]:
            l1.append(i)
    return l1
print(palindrome_numbers())
print("*"*50)
#***************************************************************************************************


# 22. Find the factorial of a number using iteration
def factorial(n):
    mul = 1
    for i in range(1,n+1):
        mul = mul * i
    return mul
print(factorial(5))
print("*"*50)
#***************************************************************************************************


# 23. Find the HCF (Highest Common Factor) of two numbers
# or greatest common divisor
def gcd():
    a,b = 8, 12
    l1=[]
    for i in range(1, min(a,b)+1):
        if a%i == 0 and b%i ==0:
            l1.append(i)
    return max(l1)
print(gcd())

# or
 
from math import gcd
a,b = 8, 12
print(gcd(a,b))
print("*"*50)
#***************************************************************************************************


# 24. Reverse the digits of a number
def reverse_number():
    a = 12345
    return int(str(a)[::-1])
print(reverse_number())
print("*"*50)
#***************************************************************************************************


# 25. Create a dictionary from two lists: one of keys and one of values
def dictionary():
    a,b = ['a', 'b', 'c'], [1, 2, 3]
    return dict(zip(a,b))
print(dictionary())

# zip() combines elements from multiple iterables (lists, tuples, etc.) position by position.
# ('name', 'Nitesh'), ('age', 25), ('city', 'Delhi')
print("*"*50)
#***************************************************************************************************


# 26. Check if two numbers are co-prime (their HCF is 1)
def co_prime():
    a,b = 8, 15
    hcf  = 0
    for i in range(1, min(a,b)+1):
        if a%i == 0 and b%i == 0:
            hcf = i
    if hcf == 1:
        print("Co-aprime")
    else :
        print("Not co-prime")
co_prime()
print("*"*50)
#***************************************************************************************************


# 27. Find the sum of all positive numbers in a list
def sum_positive():
    l1 = [-1, 2, 3, -4, 5]
    sum = 0
    for i in l1:
        if i > 0:
            sum = sum + i
    return sum
print(sum_positive())
print("*"*50)
#***************************************************************************************************


# 28. Find all perfect squares between two numbers
def perfect_square():
    a,b = 1, 100
    l1 = []
    for i in range(1,100+1):
        mul  = i**2
        l1.append(mul)
        if mul == 100:
            break
    return l1
print(perfect_square())
print("*"*50)
#***************************************************************************************************


# 29. Find the longest common prefix of a list of strings
def commom_prefix():
    str1 = ['flower', 'flow', 'flight']
        
    if not str1:
        return ""
    
    prefix = str1[0]
    for i in str1[1:]:
        while not i.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

print(commom_prefix())
print("*"*50)
#***************************************************************************************************


# 30. Find the largest palindrome made from the product of two 2-digit numbers
def largest_palindrome_number():
    max_palindrome = 0
    for i in range(10,100):
        for j in range(10,100):
            product = i*j
            if str(product) == str(product)[::-1]:
                max_palindrome = max(max_palindrome, product)
    return max_palindrome

print(largest_palindrome_number())
print("*"*50)
#***************************************************************************************************


# 31 Replace all vowels in a string with the character '*'
def replace_vowels():
    vowels = ['a','e','i','o','u']
    word = "Hello world"
    for i in word:
        for j in vowels:
            if i == j:
                word = word.replace(i,"*")
    return word

print(replace_vowels())
print("*"*50)
#***************************************************************************************************

