# DSC510
# 2.1 Programming Assignment
# Author Michelle Rice
# 09/09/20
# The purpose of this program is to estimate the cost of fiber optic installation

print("Hello. Thank you for visiting our site, we look forward to serving you."
      "\nPlease provide some information to get started.\n")

# Retrieve company name and feet of cable from customer
company = input("What is your company name?")
feet_required = float(input("How many feet of fiber optic cable do you need? (please enter numbers only)"))

# Calculate cost of installation at .87 per foot
cost = float(feet_required * .87)

# Print receipt with company name and total cost
print("\n***RECEIPT***")
print("\nCustomer: " + company)
print("Required cable =", feet_required, "feet at $0.87 per foot")
print("Total Cost = $", cost)
print("\nThank you for your business!")
