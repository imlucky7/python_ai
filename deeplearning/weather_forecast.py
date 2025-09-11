import os
import requests
from perplexity_client import PerplexityClient
from chatgpt_client import ChatGPTClient
from dotenv import load_dotenv

# Get the Weather API key from the .env file
# https://openweathermap.org/price
load_dotenv(".env", override=True)
api_key = os.getenv("WEATHER_API_KEY")

# Store the latitude value in the 'lat' variable
lat = 37.4419  # Palo Alto, CA

# Store the longitude value in the 'long' variable
lon = -122.1430

url = f"https://api.openweathermap.org/data/2.5/forecast?units=metric&cnt=1&lat={lat}&lon={lon}&appid={api_key}"

# Use the get function from the requests library to store the response from the API
response = requests.get(url)
# Take the response from the API (in JSON) and assign it to a Python dictionary
data = response.json()

# Print
print(data)

temperature = data["list"][0]["main"]["temp"]
description = data["list"][0]["weather"][0]["description"]
wind_speed = data["list"][0]["wind"]["speed"]

weather_string = f"""The temperature is {temperature}°C. 
It is currently {description},
with a wind speed of {wind_speed}m/s.
"""

print(weather_string)

prompt = f"""Based on the following weather, 
suggest an appropriate outdoor outfit.

Forecast: {weather_string}
"""
px = PerplexityClient()
response = px.ask(prompt)
print(response)

"""
gptClient = ChatGPTClient()
response = gptClient.ask(prompt)
gptClient.stream("Write a poem about AI.")
print(response)
"""
