from django.forms import ModelForm, TextInput
from .models import City, WeatherInfo

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']

# class WeatherInfo(ModelForm):
#     class Meta:
#         model = WeatherInfo
#         fields = '__all__'
#         exclude = ['weatherInfo']