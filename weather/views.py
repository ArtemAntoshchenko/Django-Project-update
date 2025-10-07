from django.shortcuts import render, redirect
from .forms import CountryForm, RussiaCityForm, USACityForm, JapanCityForm
from .models import Country
import requests

def country(request):
    form=CountryForm()
    if request.method=='POST':
        form=CountryForm(request.POST)
        if form.is_valid():
            city_name=form.cleaned_data['name']
            if city_name == 'Russia':
                return redirect('russian')
            elif city_name == 'USA':
                return redirect('usa')
            elif city_name == 'Japan':
                return redirect('japan')
    return render(request, 'choose_country.html', {'form' : form})

def Russia(request):
    form=RussiaCityForm()
    return render(request, 'choosen_city_russia.html', {'form' : form})

def USA(request):
    form=USACityForm()
    return render(request, 'choosen_city_usa.html', {'form' : form})

def Japan(request):
    form=JapanCityForm()
    return render(request, 'choosen_city_japan.html', {'form' : form})

def cityWeather(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1c9e7a15fb80db1fdb34cfb47907cec9'

    if request.method=='POST':
        if 'nameRussia' in request.POST:
            form=RussiaCityForm(request.POST)
            if form.is_valid():
                city_name=form.cleaned_data['nameRussia']
                response=requests.get(url.format(city_name)).json()
            # if City.objects.filter(name=city_name).exists():
            #     pass
            # else:
                form.save()
                # WeatherInfo.objects.create(
                #     weather=response['weather'][0]['main'], temp=response['main']['temp'], humidity=response['main']['humidity'], weatherInfo=idSave
                #     )
        elif 'nameUSA' in request.POST:
            form=USACityForm(request.POST)
            if form.is_valid():
                city_name=form.cleaned_data['nameUSA']
                response=requests.get(url.format(city_name)).json()
        elif 'nameJapan' in request.POST:
            form=JapanCityForm(request.POST)
            if form.is_valid():
                city_name=form.cleaned_data['nameJapan']
                response=requests.get(url.format(city_name)).json()
    
    city_weather={
            'city' : city_name,
            'temperature' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
        }

    context={'city_weather' : city_weather}
    return render(request, 'weather.html', context)

