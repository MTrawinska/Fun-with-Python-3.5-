import requests

provided_api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

import urllib.request, json

with urllib.request.urlopen("http://api.icndb.com/jokes/random") as url:

     data = json.loads(url.read().decode())

def joke():

        choice = input("Are you experiencing some miserable weather? Want to cheer up? Please choose 'y' to display corny joke or 'q' to quit: ")
        if choice == "q":
                print("Goodbye")
                return
        if choice == "y":
                data1 = data["value"]["joke"]
                print(data1)
                return
        if choice != "y" or n1 != "q":
                print("Please write 'next' or 'q', bye bye")
                return

city = str(input('Hello :) Please provide city name (in english pls) to enjoy my Daily Weather update:'))

try:
    url = provided_api_address + city
    json_data = requests.get(url).json()

    current_temperature = json_data['main']['temp']
    current_temperature = current_temperature - 273.15
    max_temperature = json_data['main']['temp_max']
    max_temperature = max_temperature - 273.15
    min_temperature = json_data['main']['temp']
    min_temperature = min_temperature - 273.15

    print("Current temperature is {0:.1f} [°C], where estimated max temperature for today is {0:.1f} [°C] and min temperatue {0:.1f} [°C]".format(current_temperature, max_temperature, min_temperature))

    current_pressure = json_data['main']['pressure']
    print("Current athmospheric pressure is", current_pressure, "[hPa]")

    current_humid = json_data['main']['humidity']

    rain_expectaton = json_data['weather']
    rain_fall = (rain_expectaton[0])['description']+"."

    def rainy():
        if current_humid <30:
            return("Perfect day for a walk with pumpkin latte.")
        elif current_humid <65:
            return ("It maight rain today so take your umbrella.")
        else:
            return ("Unfortunatelly, you can expect heavy rains.")

    print("In", city.capitalize(), "current humidity is", current_humid, "per cent.", rainy(), "Over the day expect some", rain_fall.lower())

    current_wind = json_data['wind']['speed']

    def windy():
        if current_wind <5:
            return("It is not windy today.")
        elif current_humid <20:
            return ("Wind speed is getting stronger.")
        else:
            return ("Unfortunatelly, you can expect storms.")

    print("In", city.capitalize(), "current wind speed is", current_wind, "km/h.", windy())
    print(" ")

    def bad_weather():
        if current_temperature < 12 and current_wind > 5.0 and current_humid > 50:
            return (joke())
        else:
            return ("Enjoy your great day!")
    print(bad_weather())

except:
    print("Please provide valid (!) city name to enjoy your weather forecast.")
