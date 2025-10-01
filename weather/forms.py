from django.forms import ModelForm, TextInput
from .models import Country, RussiaCity, USACity, JapanCity

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['name']

class RussiaCityForm(ModelForm):
    class Meta:
        model = RussiaCity
        fields = ['nameRussia']

class USACityForm(ModelForm):
    class Meta:
        model = USACity
        fields = ['nameUSA']

class JapanCityForm(ModelForm):
    class Meta:
        model = JapanCity
        fields = ['nameJapan']

