house_rent = float(input("Enter the total rent amount: "))
electricity_unit_used = float(input("Enter the electricity units used: "))
per_unit_charge = float(input("Enter the per unit charge for electricity: "))
total_people = int(input("Enter the total number of people sharing the rent: "))

# Now, we can calculate the total electricity charge and the total amount due.
total_electricity_charge = electricity_unit_used * per_unit_charge
total_rent = house_rent + total_electricity_charge

# Finally, we can calculate the amount each person needs to pay.
amount_per_person = total_rent / total_people
print("*" * 50)
print("--- Rent Calculation ---")


print(f"Total electricity charge: {total_electricity_charge}")
print(f"Total rent amount: {total_rent}")
print(f"Amount each person needs to pay: {amount_per_person}")