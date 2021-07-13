# DSC510
# 4.1 Programming Assignment
# Author Michelle Rice
# 09/27/20
# The purpose of this program is to estimate the cost of fiber optic
# installation including a bulk discount

from decimal import Decimal

print('Hello. Thank you for visiting our site, we look forward to serving you.'
      '\nPlease provide some information to get started.\n')

# Retrieve company name and feet of cable from customer
company = input("What is your company name?")
feetRequired = float(input("How many feet of fiber optic cable do you need? (please enter numbers only)"))
# Set price tier
price1 = .87
price2 = .80
price3 = .70
price4 = .50

# Determine price based on requested feet of cable
if feetRequired > 500:
    discPrice = price4
elif 250 < feetRequired <= 500:
    discPrice = price3
elif 100 < feetRequired <= 250:
    discPrice = price2
else:
    discPrice = price1


# Calculate total cost
def calculate(feet, price):
    cost = feet * price
    return cost


totalCost = calculate(feetRequired, discPrice)


# Print receipt with company name and total cost
print("\n***RECEIPT***")
print("\nCustomer: " + company)
print("Required cable =", feetRequired, "feet at $", "{:.2f}".format(discPrice), "per foot")
print("Total Cost = $", "{:.2f}".format(totalCost))
print("\nThank you for your business!")
