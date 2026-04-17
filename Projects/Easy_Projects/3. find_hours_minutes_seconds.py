# WAP to get remaining hours, minutes and seconds from the total seconds of the day


# Enter time  : 08:30

## ------------ Remaining Time ------------

# current_time = input("Enter time (HH:MM): ")
current_time = "08:30"

# Total time spend
spend_hours = int(current_time[0:2])
# print("Spend hours:", spend_hours)
spend_minutes = int(current_time[3:5])
# print("Spend minutes:", spend_minutes)
spend_seconds = (spend_hours * 3600) + (spend_minutes * 60)
# print("Spend seconds:", spend_seconds)

# total seconds in a day
total_seconds = 24 * 3600
print("Total seconds in a day:", total_seconds)

# Remaining time
remaining_seconds = total_seconds - spend_seconds
remaining_hours = remaining_seconds // 3600
remaining_minutes = remaining_seconds // 60

print("Remaining hours:", remaining_hours)
print("Remaining minutes:", remaining_minutes)
print("Remaining seconds:", remaining_seconds)