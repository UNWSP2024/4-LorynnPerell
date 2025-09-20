# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
    budget = float(input("Enter your month budget: "))
    total_expenses = 0.0

    while True:
        expense = float(input("Enter an expense ( or 0 to finish): "))
        if expense == 0:
            break
        total_expenses += expense

    print("\--- Budget Report ---")
    if total_expenses > budget:
        print(f"You are over budget by ${total_expenses - budget: .2f}")
    elif total_expenses < budget:
        print(f"You are under budget by ${budget - total_expenses: .2f}")
    else:
        print("You are exactly on budget")
    ######################


if __name__ == '__main__':
    main()