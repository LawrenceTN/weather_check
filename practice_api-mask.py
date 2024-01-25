import requests

weather_api_key = "************************"
api_ninja_key = "************************"

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

weather_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={weather_api_key}&units=imperial"
response = requests.get(weather_url)
weather_data = response.json()
print(weather_data)
# temperature = weather_data['main']['temp']
# print(f"Current temperature: {temperature}")