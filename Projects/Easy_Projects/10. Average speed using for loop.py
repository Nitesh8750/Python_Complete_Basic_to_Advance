usain_bolt = [10.03, 9.69, 9.58, 11.44, 9.76, 9.63, 9.77, 9.98, 9.79, 9.81, 9.95]


min = usain_bolt[0]
max = usain_bolt[0]
sum = 0
for i in usain_bolt:
    # minimum = min(usain_bolt)
    # maximum = max(usain_bolt)
    if i < min :
        min = i
    if i > max :
        max = i
    # average = round(sum(usain_bolt)/len(usain_bolt),2)
    
    sum = sum + i
    length = len(usain_bolt)
    average = round(sum/length, 2)

print(f"The minimum speed of Usain bolt is {min} km/hr")
print(f"The maximum speed of Usain bolt is {max} km/hr")
print("sum", round(sum, 2))

print(f"The Average speed of Usain bolt is {average} km/hr")