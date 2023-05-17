from django.shortcuts import render
from datetime import datetime
import requests
import json

def index(request):
    return render(request, 'WeatherApp/index.html')

def get_current_weather(request):
    city = request.GET.get('city')
    if city:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=021d9f00020d0e7699950fd1a03ee23c&units=metric'
        response = requests.get(url)
        weather_data = json.loads(response.text)
        temp = weather_data['main']['temp']
        message = f"The current temperature in {city} is {temp}°C."
    else:
        message = "Please enter a city name in the search box."
    return render(request, 'weatherApp/index.html', {'message': message,'temp': temp,'city': city})