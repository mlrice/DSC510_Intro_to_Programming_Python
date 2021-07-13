# DSC510
# Week 10
# 10.1 Programming Assignment
# Author Michelle Rice
# 11/7/20
# This program asks the user if they would like to read a joke, if yes
# it calls an API and returns a joke to them, and repeats until they say no

import requests
import json


def main():
    while True:
        first_joke = input("Would you like to receive a Chuck Norris joke? Y/N")

        # function to produce another joke if the user desires or print
        # a message and quit if they don't
        def another_joke():
            another = input("Would you like another joke? Y/N")
            if another.upper() == 'Y':
                jokes()
            elif another.upper() == 'N':
                print("Hope you enjoyed your laughs! Goodbye!")
            else:
                print("Please enter Y or N")
                another_joke()

        # function to call the API and return a joke and call the function
        # that asks if they would like another joke
        def jokes():
            response = requests.get("http://api.icndb.com/jokes/random")
            joke = json.loads(response.text)
            print(joke["value"]["joke"])
            another_joke()

        # determine if the user wants to read a joke and either call the function
        # or print a message and quit the program.  If they provide an invalid response
        # print a message and ask again
        if first_joke.upper() == 'Y':
            jokes()
        elif first_joke.upper() == 'N':
            print("Thanks, have a great day!")
        else:
            print("Please make sure you answer with Y or N")
            continue

        break


if __name__ == "__main__":
    main()



