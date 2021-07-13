# DSC510
# Week 5
# 5.1 Programming Assignment
# Author Michelle Rice
# 10/2/20
# The purpose of this program is to obtain input from
# the user and run various calculations on the input

def main():
    while True:
        operator = input("Would you like to add, subtract, multiply, divide, or calculate Average? "
                         "\nEnter 1 to add, 2 to subtract, 3 to multiply, 4 to divide, or 5 for average: ")

# function to get input from user and calculate average
        def calculateAverage():
            numRequested = int(input("How many numbers would you like to average?"))
            inputs = []
            for i in range(0, numRequested):
                userNums = int(input("Please enter a number"))
                inputs.append(userNums)

            avg = sum(inputs) / numRequested

            return avg

# function to get input from user and calculate solution based on selected operator
        def performCalculation(choice):
            input1 = float(input("Please enter a number: "))
            input2 = float(input("Please enter another number: "))

            if operator == "1":
                calc = input1 + input2
            elif operator == "2":
                calc = input1 - input2
            elif operator == "3":
                calc = input1 * input2
            elif operator == "4":
                calc = input1 / input2
            return calc

# call appropriate funciton based on user input, return to beginning if user does not enter 1-5
        if operator == "5":
            average = calculateAverage()
            print ("The average of the numbers you entered is:", average)

        elif 1 <= int(operator) <= 4:
            solution = performCalculation(operator)

            print ("Your calculation is:", solution)
        else:
            continue

        finish = input("Would you like to continue? Y/N")

# if user does not wish to continue, end program, if they do, start over
        if finish == 'N':
            print ("Goodbye")
            break


if __name__ == "__main__":
    main()
