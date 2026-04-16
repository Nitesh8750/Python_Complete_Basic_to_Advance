# WAP to Calculate Simple Interest with User Input Validation and Loop

principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

simple_interest = (principle * rate * time) / 100
total_amount = principle + simple_interest
print(f"The simple interest is: {simple_interest}")
print(f"The total amount is: {total_amount}")







# Created by Claude in VS code chat-box
# By Using the following code, 
# you can create a simple interest calculator that includes user input validation and 
# allows the user to perform multiple calculations in a loop:


# def get_positive_number(prompt):
#     """
#     Get a positive number from user with validation.
#     Keeps prompting until valid input is received.
#     """
#     while True:
#         try:
#             value = float(input(prompt))
#             if value <= 0:
#                 print("Error: Please enter a positive number greater than 0.\n")
#                 continue
#             return value
#         except ValueError:
#             print("Error: Please enter a valid number.\n")


# def calculate_simple_interest(principal, rate, time):
#     """
#     Calculate simple interest and total amount.
#     Formula: SI = (P × R × T) / 100
#     Total Amount: A = P + SI
#     """
#     simple_interest = (principal * rate * time) / 100
#     total_amount = principal + simple_interest
#     return simple_interest, total_amount


# def main():
#     """
#     Main function to run the simple interest calculator with loop.
#     """
#     print("=" * 50)
#     print("    SIMPLE INTEREST CALCULATOR")
#     print("=" * 50)
#     print()
    
#     while True:
#         # Get user inputs with validation
#         principal = get_positive_number("Enter Principal Amount (P): $")
#         rate = get_positive_number("Enter Rate of Interest per Annum (R) in %: ")
#         time = get_positive_number("Enter Time Period (T) in years: ")
        
#         # Calculate simple interest and total amount
#         si, total = calculate_simple_interest(principal, rate, time)
        
#         # Display results
#         print("\n" + "-" * 50)
#         print("CALCULATION RESULTS:")
#         print("-" * 50)
#         print(f"Principal Amount (P):        ${principal:,.2f}")
#         print(f"Rate of Interest (R):        {rate}% per annum")
#         print(f"Time Period (T):             {time} years")
#         print(f"Simple Interest (SI):        ${si:,.2f}")
#         print(f"Total Amount (A):            ${total:,.2f}")
#         print("-" * 50)
#         print()
        
#         # Ask user if they want to continue
#         while True:
#             choice = input("Do you want to calculate another interest? (yes/no): ").strip().lower()
#             if choice in ['yes', 'y']:
#                 print("\n" + "=" * 50 + "\n")
#                 break
#             elif choice in ['no', 'n']:
#                 print("\nThank you for using Simple Interest Calculator!")
#                 print("=" * 50)
#                 return
#             else:
#                 print("Error: Please enter 'yes' or 'no'.\n")


# if __name__ == "__main__":
#     main()
