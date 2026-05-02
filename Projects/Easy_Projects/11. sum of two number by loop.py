# find the sum of two numbers from 1 to 100 and evenly divisible by 5

num = 0
for i in range(1, 101):
    if i % 5 == 0 :
        num = num + i
print(num)

