# Expense-Tracker - Installment 1
# Author: Christian Mark T. Buquel
# A personal expense tracker landing page

print("-" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("-" * 40)

print("\nWelcome! This is your personal expense tracker.\n")

print("MAIN MENU")
print("\t[1] Add an expense\t(coming soon)")
print("\t[2] View all expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

tax_rate = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

tax = total * (tax_rate / 100)
grand_total = total + tax
over_budget = grand_total > budget
left_in_budget = budget - grand_total

print("-" * 50)
print("SUMMARY")
print(f"- {item1}:       ${amount1:.2f}")
print(f"- {item2}:       ${amount2:.2f}")
print(f"Subtotal:        ${total:.2f}")
print(f"Average:         ${average:.2f}")
print(f"Tax ({tax_rate:.1f}%):     ${tax:.2f}")
print(f"Grand total:     ${grand_total:.2f}")
print(f"Over budget?     {over_budget}")
print(f"Left in budget:  ${left_in_budget:.2f}")
print("-" * 50)
print(f"Made by: {name} | Installment 3")

