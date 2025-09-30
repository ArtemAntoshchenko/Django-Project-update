from django.shortcuts import render
from .forms import CityForm
from .models import City
import requests

# def index(request):
#     if request.method=='POST':
#         city_name=request.POST.get('city')
#     return render(request, 'choose_city.html')

def cityWeather(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1c9e7a15fb80db1fdb34cfb47907cec9'

    if request.method=='POST':
        form=CityForm(request.POST)
        form.save()

    form=CityForm()
    cities=City.objects.all()
    weather_data=[]
    
    for city in cities:
        response=requests.get(url.format(city)).json()
        city_weather={
            'city' : city,
            'temperature' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context={'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather.html', context)

