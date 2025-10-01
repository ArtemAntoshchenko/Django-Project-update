from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

class WeatherInfo(models.Model):
    weather = models.CharField(max_length=10)
    temp = models.IntegerField()
    humidity = models.IntegerField(default=0)
    wind_speed = models.IntegerField(default=0)
    weatherInfo = models.OneToOneField('City', on_delete=models.CASCADE, primary_key=True)
