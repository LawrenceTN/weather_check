import requests
import webbrowser
import pprint
from bs4 import BeautifulSoup

weather_api_key = "************************"
api_ninja_key = "************************"

def open_pinterest(clothes):
    url = f'https://www.pinterest.com/search/pins/?q={clothes}'
    response = requests.get(url)

    if response.status_code == 200: # If response is valid
        soup = BeautifulSoup(response.content, 'html.parser')
        search_bar = soup.find('input', {'class': 'typeaheadInput'})

        if search_bar:
            search_bar['value'] = clothes
            search_url = f'https://www.pinterest.com/search/pins/?q={search_bar["value"]}'
            webbrowser.open(search_url)
        else:
            print("Search bar isn't found.")
    else:
        print("This page is not online")
    return

# Function to check if user input is a zip code (num) or city (string)
def is_number(user_input):
    if user_input.isdigit():
        return True
    else:
        return False

# The user will enter their city name OR zip codeand it will spit out the weather information
user_input = input("Please enter a city or zip code: ")

if is_number(user_input):
    zip_url = f"https://api.api-ninjas.com/v1/zipcode?zip={user_input}"
    response = requests.get(zip_url, headers={'X-Api-Key': api_ninja_key})
    zip_data = response.json()[0]
    lat = zip_data['lat']
    lon = zip_data['lon']
else:
    city_url = f"https://api.api-ninjas.com/v1/city?name={user_input}"
    response = requests.get(city_url, headers={'X-Api-Key': api_ninja_key})
    city_data = response.json()[0] # response.json is a list made of 1 dict collection of items
    lat = city_data['latitude']
    lon = city_data['longitude']

# Floats
print(f"Lattitude = {lat}\nLongitude = {lon}\n") 

weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}&units=imperial"
response = requests.get(weather_url)
weather_data = response.json()
# pprint.pprint(weather_data)

# Extract the weather temperature and feels like
feels_like = weather_data['main']['feels_like']
temp = weather_data['main']['temp']
description = weather_data['weather'][0]['description']

print(f"Feels like: {feels_like}F")
print(f"Temp is: {temp}")
print(f"Looks like: {description}")

if feels_like <= 73:
    clothes = 'cloudy clothes'
else:
    clothes = 'summer clothes'

print(f"Let's look for {clothes}")

open_pinterest(clothes)
