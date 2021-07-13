# DSC510
# Week 6
# 6.1 Programming Assignment
# Author Michelle Rice
# 10/8/20
# The purpose of this program is to obtain temperatures from the
# user and determine the number of temps, largest and smallest temp

def main():
    while True:

        temperatures = []

        n = (input("Enter number of temperatures you would like to compare: "))

        if n.isdigit():

            i = 0
            while i < int(n):
                temp = (input("Please enter a temperature: "))
                if temp.isdigit():
                    temperatures.append(temp)
                    i += 1
                    print(temperatures[-0])
                else:
                    i += 0
                    print("Your temperature must be a number, please try again.")

            message = "You have entered a total of " + str(len(temperatures)) + " temperatures."
            print ("\nMaximum temperature entered is: ", max(temperatures))
            print ("\nMinimum temperature entered is: ", min(temperatures))
            print ("\n" + message)
            break

        else:
            print ("You must enter a number.  Please try again.")
            continue


if __name__ == "__main__":
    main()
