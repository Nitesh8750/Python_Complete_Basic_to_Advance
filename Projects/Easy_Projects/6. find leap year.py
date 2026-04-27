year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# This code takes a year as input and checks if it is a leap year or not. A leap year is defined as:
# - It is divisible by 4 but not divisible by 100, OR
# - It is divisible by 400.
# For example:
# - 2020 is a leap year because it is divisible by 4 and not divisible by 100.
# - 1900 is not a leap year because it is divisible by 100 but not divisible by 400.
# - 2000 is a leap year because it is divisible by 400.