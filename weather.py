# DSC510
# Week 12
# 12.1 Final Project
# Author Michelle Rice
# 11/20/20
# This program asks the user for to input a zip or city into
# a weather app and prints current conditions

import requests


# evaluate user input as zip or city and append the value to the
# appropriate api based on input and return that portion of the url
def get_location(user_loc):
    if user_loc.isdigit():
        location = ("zip=" + user_loc + ",us&units=imperial&appid=a9a40bb90b86bd3da57d3c9c211356cd")
    else:
        location = ("q=" + user_loc + "&units=imperial&appid=a9a40bb90b86bd3da57d3c9c211356cd")
    return location


# this function takes in the portion of the url created in get_location
# and adds it to the base url and checks for valid api response
# if invalid response is received, return user to (main) to start over
def get_response(location):
    try:
        r = requests.get("http://api.openweathermap.org/data/2.5/weather?" + location)
        if r.status_code == 200:
            response = r.json()
            return response
        else:
            raise Exception

    except Exception:
        print("Invalid entry, please try again")
        exit(main())


# takes the full url from get_location and uses that to access the fields in the
# API, identifies fields and prints
def get_weather(response):
    weather = response
    forecast = weather["main"]
    current_temp = forecast["temp"]
    feels_like = forecast["feels_like"]
    high = forecast["temp_max"]
    low = forecast["temp_min"]
    pressure = forecast["pressure"]
    humidity = forecast["humidity"]
    clouds = weather["clouds"]
    cloud_cover = clouds["all"]
    print("Current Temperature: ", int(current_temp), "degrees")
    print ("Feels Like: ", int(feels_like), "degrees")
    print ("Atmospheric pressure: ", int(pressure))
    print ("Humidity: ", humidity, "%")
    print("Cloud Cover: ", cloud_cover, "%")
    print("High Temperature: ", int(high), "degrees")
    print("Low Temperature: ", int(low), "degrees")


# takes user input and calls get_location, get_response and get_weather
# continues doing this until user inputs exit set to (.title to avoid errors)
def main():
    while True:
        user_loc = input("\nPlease enter your Zip, City or Exit to exit the app: ")
        if user_loc.title() == "Exit":
            print("Goodbye!")
            break
        else:
            location = get_location(user_loc)
            response = get_response(location)
            print("\nCurrent conditions for " + user_loc.title() + ":\n")
            get_weather(response)


if __name__ == "__main__":
    main()









