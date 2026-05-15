# 1. Check if all elements in a list are unique
"""
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
"""


# 9 