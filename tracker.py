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

print("-" * 40)
print("SUMMARY")
print(f"{item1:<15} ${amount1:.2f}")
print(f"{item2:<15} ${amount2:.2f}")
print(f"{'Total spent:':<15} ${total:.2f}")
print(f"{'Average:':<15} ${average:.2f}")
print("-" * 40)

print(f"Made by: {name} | Installment 2")