from django.shortcuts import render, redirect
from .forms import CityForm
from .models import City, WeatherInfo
import requests

def index(request):
    form=CityForm()
    return render(request, 'choose_city.html', {'form' : form})

def cityWeather(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1c9e7a15fb80db1fdb34cfb47907cec9'

    if request.method=='POST':
        form=CityForm(request.POST)
        if form.is_valid():
            city_name=form.cleaned_data['name']
            if City.objects.filter(name=city_name).exists():
                pass
            else:
                form.save()

    response=requests.get(url.format(city_name)).json()
    # WeatherInfo.objects.

    city_weather={
            'city' : city_name,
            'temperature' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
        }

    context={'city_weather' : city_weather}
    return render(request, 'weather.html', context)

