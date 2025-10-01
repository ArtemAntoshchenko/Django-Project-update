from django.db import models

choiceCountry = [
    ('Russia', 'Russia'),
    ('USA', 'USA'),
    ('Japan', 'Japan'),
]

choiceCityRussia = [
    ('Moscow', 'Moscow'),
    ('Sochi', 'Sochi'),
]

choiceCityUSA = [
    ('New York', 'New York'),
    ('Las Vegas', 'Las Vegas'),
]

choiceCityJapan = [
    ('Tokyo', 'Tokyo'),
    ('Kioto', 'Kioto'),
]

class Country(models.Model):
    name = models.CharField(max_length=25, choices=choiceCountry, default='Russia')
    
    def __str__(self):
        return self.name


class RussiaCity(models.Model):
    nameRussia = models.CharField(max_length=25, choices=choiceCityRussia, default='Sochi')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

class USACity(models.Model):
    nameUSA = models.CharField(max_length=25, choices=choiceCityUSA, default='New York')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

class JapanCity(models.Model):
    nameJapan = models.CharField(max_length=25, choices=choiceCityJapan, default='Tokyo')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

# class WeatherInfo(models.Model):
#     weather = models.CharField(max_length=10)
#     temp = models.IntegerField()
#     humidity = models.IntegerField(default=0)
#     wind_speed = models.IntegerField(default=0)
#     weatherInfo = models.OneToOneField('RussiaCity', on_delete=models.CASCADE, primary_key=True)
