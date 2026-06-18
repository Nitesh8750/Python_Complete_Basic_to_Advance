"""
A Python dictionary is a mutable object that stores data as key-value pairs, 
with each key separated from its value by a colon (:). 
Dictionary is the most widely used data structure, 
and it is necessary to understand its methods and operations."""


# 1. WAP to add a new key-value pair to a dictionary, modify an existing value, and access a specific key.
student = {"name": "Alice", "age": 20, "grade": "B"}
print(student)

# add a specific key : value pair
student["city"] = "New York"
print(student)

# modify age
student["age"] = 21
print(student)

# access a specific key
print(student["name"])

print("*"*50)
#************************************************************************************************


# 2. WAP to remove a specific key from a dictionary, retrieve all key-value pairs, and check whether a given key exists.
car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}

# remove a specific
car.pop("brand")
print(car)
# pop() is used to remove a specific key-value pair

# retrieve all keys-value pairs
print(car.items())

# Check key existence
print("brand" in car)
print("color" in car)

print("*"*50)
#************************************************************************************************


# 3. WAP to create a dictionary by mapping two equal-length lists, one containing keys and the other containing values.
keys = ["name", "age", "city"]
values = ["Bob", 25, "London"]

employee = dict(zip(keys, values))
print(employee)

# zip(keys, values) id used to pair elements from both lists by index.
print("*"*50)
#************************************************************************************************


# 4. WAP to remove all items from a dictionary while keeping the dictionary object itself intact.
inventory = {"apples": 10, "bananas": 5, "oranges": 8}

inventory.popitem()
print(inventory)
# popitem() is used to remove the last key-value

inventory.clear()
print(inventory)

print("*"*50)
#************************************************************************************************


# 5. WAP to combine two dictionaries into a single dictionary. If both dictionaries share a key, the value from the second dictionary should take precedence.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)

#Method 2: unpacking — creates a new dictionary
dict1 = {"a": 1, "b": 2}
merged = {**dict1, **dict2}
print(merged)

# Method 3: merge operator (Python 3.9+)
dict1 = {"a": 1, "b": 2}
merged = dict1 | dict2
print(merged)

print("*"*50)
#************************************************************************************************


# 6. WAP to retrieve a specific value from a dictionary that is nested inside another dictionary.
person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
print(person["address"]["city"])

# or
city = person["address"]["city"]
print(city)

print("*"*50)
#************************************************************************************************


# 7. WAP to access the value associated with the key 'history' from a dictionary nested within a larger data structure.
student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}

history = student["grades"]["history"]
print(history)
print(student["grades"]["history"])

print("*"*50)
#************************************************************************************************


# 8. WAP to create a dictionary from a list of keys, assigning the same default value to every key.
keys = ["math","science","english","hindi"]
default = 0

subject = dict.fromkeys(keys, default)
print(subject)

# dict.fromkeys(keys, default) : when we want to assign same default values to all keys
print("*"*50)
#************************************************************************************************


# 9. WAP to rename an existing key in a dictionary while preserving its associated value and the rest of the dictionary unchanged.
employee = {"fname": "John", "age": 30, "dept": "Engineering"}

employee["First_name"] = employee.pop("fname")

print(employee)
print("*"*50)
#************************************************************************************************


# 10. WAP to remove multiple specific keys from a dictionary in one operation.
product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}

number = int(input("how many keys you want to remove:"))
for i in range(number):
    key = input(f"enter the key {i+1}:")
    
    if key in product:
        product.pop(key)
    else :
        print(f"{key} not found")
print(product)
print("*"*50)
#************************************************************************************************


# 11. WAP to verify whether a specific value is present anywhere in a dictionary.
roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}
print(roles.values())

value = input("enter key:")
if value in roles.values():
    print(f"{value} present")
else:
    print(f"{value} not found")

# roles.values() : it used to print all values of a dictionary
print("*"*50)
#************************************************************************************************


# 12. WAP to calculate the total of all numerical values stored in a dictionary.
expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}
sum = 0
print(expenses.values())

for i in expenses.values():
    sum = sum + i
print(sum)
print("*"*50)
#************************************************************************************************
    

# 13. WAP to create a new dictionary containing only a specified subset of keys from an existing dictionary.
user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}
user_details = {}
user_details["id"] = user["id"]
user_details["username"] = user["username"]
user_details["email"] = user["email"]
print(user_details)

# OR

keys_to_keep = ["id", "username", "email"]
subset = {}
for i in keys_to_keep:
    subset[i] = user[i]
print(subset)
print("*"*50)
#************************************************************************************************


# 14. WAP that uses zip() to combine a list of keys and a list of values into a single dictionary.
attributes = ["brand", "model", "year", "color"]
details = ["Honda", "Civic", 2023, "silver"]

print(dict(zip(attributes,details)))
print("*"*50)
#************************************************************************************************


# 15. WAP to count how many times each character appears in a given string, storing the results in a dictionary.
text = "hello world"

freq = {}
for i in text:
    c = text.count(i)
    freq[i] = freq.get(f"{i} :",c)
print(freq)

# or

freq = {i : text.count(i) for i in text}
print(freq)
print("*"*50)
#************************************************************************************************


# 16. WAP to change a specific value inside a dictionary that is nested within another dictionary.
company = {"name": "TechCorp", "location": {"city": "Berlin", "country": "Germany"}}

company["location"]["city"] = "Munich"

print(company)
print("*"*50)
#************************************************************************************************


# 17. WAP to update a value located multiple levels deep inside a nested dictionary structure.
data = {"school": {"department": {"class": {"teacher": "Mr. Smith", "students": 30}}}}

data["school"]["department"]["class"]["students"] = 35
print(data)
print("*"*50)
#************************************************************************************************


# 18. WAP to generate a dictionary of the squares of numbers from 1 to 10 using a dictionary comprehension in a single line.
square = {}
for i in range(1,11):
    square[i] = square.get(f"{i} : ", i**2)
print(square)

# or

sqauare = {i : i**2 for i in range(1,11)}
print(square)
print("*"*50)
#************************************************************************************************


# 19. WAP to create a new dictionary containing only the key-value pairs from an existing dictionary where the value meets a specified condition.
scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}
new_scores = {k : v for k,v in scores.items() if v > 60}
print(new_scores)
print("*"*50)
#************************************************************************************************


# 20. WAP to find the key associated with the smallest numerical value in a dictionary.
stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
print(min(stock.values()))

minimum = min(stock, key=stock.get)
print(minimum)

# or 

lowest = min(stock.values())
minimum_key = [k for k,v in stock.items() if v == lowest]
print(minimum_key)
print("*"*50)
#************************************************************************************************


# 21. WAP to find the key associated with the highest numerical value in a dictionary.
scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}

maximum = max(scores, key=scores.get)
print(maximum)

# or

highest = max(scores.values())
highest_key = [key for key,value in scores.items() if value == highest]
print(highest_key)
print("*"*50)
#************************************************************************************************


# 22. WAP to convert a list of key-value tuples into a dictionary without using any loops.
pairs = [("name", "Alice"), ("age", 25), ("city", "Paris")]

duct1 = dict(pairs)
print(duct1)
print("*"*50)
#************************************************************************************************


# 23. WAP to identify all keys that are present in both of two given dictionaries.
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}

l1 = []

for i in d1.keys():
    for j in d2.keys():
        if i == j:
            l1.append(i)
print(l1)

# or

common_keys = d1.keys() & d2.keys()
print(common_keys)
print("*"*50)
#************************************************************************************************


# 24. WAP to find all keys that exist in the first dictionary but are absent from the second dictionary.
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "d": 40}

l1 = []

for i in d1.keys():
    if i not in d2.keys():
        l1.append(i)        
print(l1)
print("*"*50)
#************************************************************************************************


# 25. WAP to create a new dictionary containing only the key-value pairs that are identical in both input dictionaries.
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"a": 1, "b": 99, "c": 3}

d3 = {k : d1[k] for k in d1.keys() & d2.keys() if d1[k] == d2[k]}
print(d3)

# or

d3 = ()
for i in d1.items():
    for j in d2.items():
        if i == j:
            d3 = d1.items() & d2.items()
print(dict(d3))
print("*"*50)
#************************************************************************************************


# 26. WAP to count the frequency of each word in a string, treating words case-insensitively so that “The” and “the” are counted as the same word.
text = "the cat sat on the mat the cat"
text1 = text.lower()
c =(text1.split())
print(text1)

dict1 = {i : c.count(i) for i in c}
print(dict1)
print("*"*50)
#************************************************************************************************


# 27. WAP to remove all key-value pairs from a dictionary where the value is None.
data = {"name": "Alice", "age": None, "city": "Paris", "score": None}

dict1 = {k : v for k,v in data.items() if v != None}
print(dict1)
print("*"*50)
#************************************************************************************************


# 28. WAP to sort a dictionary by its keys and return the result as a new dictionary with items in ascending key order.
data = {"banana": 3, "apple": 5, "cherry": 1, "date": 4}

dict1 = dict(sorted(data.items()))
print(dict1)
print("*"*50)
#************************************************************************************************


# 29 Write a Python program to sort a dictionary’s items based on their values in ascending order.
scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}

scores = dict(sorted(scores.items(), key = lambda item : item[1]))
print(scores)
# key=lambda item: item[1]: Tells sorted() to compare items by their second element (the value), not the key.
print("*"*50)
#************************************************************************************************


# 30. WAP to check whether all values in a dictionary are distinct (i.e., no two keys share the same value).
data = {"a": 1, "b": 2, "c": 3, "d": 2}

value = data.values()
print(value)
if (len(value) == len(set(value))):
    print("values are distinct")
else :
    print("values are duplicates")
print("*"*50)
#************************************************************************************************


# 31. WAP to verify whether one dictionary is a subset of another, meaning all key-value pairs of the smaller dictionary exist in the larger one.
main = {"a": 1, "b": 2, "c": 3, "d": 4}
subset = {"a": 1, "c": 3}

if subset.items() <= main.items():
    print("subset is present in main dict")
else :
    print("subset is not present in main dict")
    
# or

if set(subset).issubset(set(main)):
    print("subset is present in main dict")
else :
    print("subset is not present in main dict")
print("*"*50)
#************************************************************************************************


# 32. Write a Python program to sort a dictionary’s items by the length of their string values, from shortest to longest.
words = {"a": "banana", "b": "kiwi", "c": "strawberry", "d": "fig"}

words = dict(sorted(words.items(), key = lambda key : len(key[1])))
print(words)
print("*"*50)
#************************************************************************************************


# 33. WAP to find the key in a dictionary whose associated list value has the greatest number of elements.
data = {"vegs": ["carrot"], "grains": ["rice", "wheat"],"fruits": ["apple", "banana", "cherry"]}

words = max(data.items(), key = lambda key : len(key[1]))[0]
print(words)
print("*"*50)
#************************************************************************************************


# 34. WAP to convert a nested dictionary into a formatted JSON string with readable indentation.
import json
person = {"name": "Alice", "age": 30, "address": {"city": "Mumbai", "pin": "400001"}}

word = json.dumps(person, indent=4)
print(word)
print("*"*50)
#************************************************************************************************


# 35. WAP to invert a dictionary by swapping its keys and values, so each original value becomes a key and each original key becomes the corresponding value.
original = {"a": 1, "b": 2, "c": 3}

dit1 = {v : k for k,v in original.items()}
print(dit1)
print("*"*50)
#************************************************************************************************


# 36. WAP to invert a dictionary where multiple keys may share the same value. Instead of overwriting, group all original keys that map to the same value into a list under that value as the new key.
original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}

inverted = {}
for k,v in original.items():
    inverted.setdefault(v,[]).append(k)
print(inverted)
# inverted.setdefault(v, []): Checks if v already exists as a key in inverted. If not, it inserts it with an empty list as the default value and returns that list either way.
# .append(k): Adds the original key to the list associated with that value, so all keys sharing the same value are collected together.
print("*"*50)
#************************************************************************************************


# 37. WAP to flatten a multi-level nested dictionary into a single-level dictionary, joining nested keys with a dot separator to form the new keys.
nested = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}}}

def flatten(d, prefix=""):
    result = {}
    for k,v in d.items():
        new_key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            result.update(flatten(v , new_key))
        else:
            result[new_key] = v
    return result
print(flatten(nested))

# prefix="": The default empty string means top-level keys get no dot prepended. As recursion deepens, the prefix carries the accumulated path of parent keys.
# new_key = f"{prefix}.{k}" if prefix else k: Builds the dotted path for the current key. At the top level it is just k; at deeper levels it becomes something like b.d.
# isinstance(v, dict): Checks whether the current value is another dictionary. If so, the function calls itself with the nested dict and the updated prefix, then merges the results with result.update().
print("*"*50)
#***************************************************************************


# 38. WAP to organize a list of words into a dictionary where each key is a starting letter and the corresponding value is a list of all words beginning with that letter.
words = ["apple", "avocado", "banana", "blueberry", "cherry", "apricot"]

grouped = {}
for i in words:
    letter = i[0]
    grouped.setdefault(letter, []).append(i)
print(grouped)
# grouped.setdefault(letter, []): Returns the existing list for that letter if it already exists, or inserts a fresh empty list and returns it if the letter is seen for the first time.
print("*"*50)
#***************************************************************************


# 39. WAP to merge two dictionaries such that when both share the same key, their values are added together rather than one overwriting the other.
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 25}

merged = dict1.copy()
for k,v in dict2.items():
    merged[k] = merged.get(k,0) + v
print(merged)
print("*"*50)
#***************************************************************************



# 40. WAP that demonstrates the difference between a shallow copy and a deep copy of a dictionary containing nested lists, showing how changes to nested data affect each copy differently.
original = {"name": "Alice", "scores": [90, 85, 92]}

import copy

original = {"name": "Alice", "scores": [90, 85, 92]}

# Shallow copy
shallow = original.copy()
shallow["scores"].append(100)
print("Shallow copy scores:", shallow["scores"])
print("Original scores after shallow mutation:", original["scores"])

print()

# Restore original for a clean deep copy demo
original = {"name": "Alice", "scores": [90, 85, 92, 100]}

# Deep copy
deep = copy.deepcopy(original)
deep["scores"].append(99)
print("Deep copy scores:", deep["scores"])
print("Original scores after deep mutation:", original["scores"])