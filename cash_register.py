# DSC510
# Week 11
# 11.1 Programming Assignment
# Author Michelle Rice
# 11/13/20
# This program asks the user for input into a cash register
# totals the count and dollar amount of the cart and prints to the user

import locale


class CashRegister:

    def __init__(self):
        self.total = 0.00
        self.items = 0

    def add_items(self, price):
        self.total = self.total + float(price)
        self.items = self.items + 1

    def get_total(self):
        locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
        total = locale.currency(self.total, grouping=True)
        return total

    def get_count(self):
        count = self.items
        return count

    def clearCart(self):
        self.total = 0.0
        self.items = 0


print ("Welcome to Shop Mart!")


def main():

    register = CashRegister()
    while True:
        price = (input("\nPlease enter the price of your item, empty to clear your cart or exit to complete your order\nPrice $"))
        if price == "exit":
            register.get_count()
            register.get_total()
            print("\nItems purchased:", register.get_count())
            print("Total sale: ", register.get_total())
            break

        elif price == "empty":
            register.clearCart()
            register.get_count()
            print("\nYou have ", register.get_count(), "items in your cart")
            register.get_total()
            print("Your current total is: $", register.get_total())

        else:
            register.add_items(price)
            register.get_count()
            print("\nYou have ", register.get_count(), "items in your cart")
            register.get_total()
            print("Your current total is: $", register.get_total())

    print("\nThanks for shopping with us.  Have a great day!")

    register.clearCart()


if __name__ == "__main__":
    main()
