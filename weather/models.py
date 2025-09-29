from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

class WeatherInfo(models.Model):
    data = models.DateTimeField()
    weather = models.CharField(max_length=25)
    temp = models.IntegerField()
    weatherInfo=models.OneToOneField('WeatherInfo', on_delete=models.CASCADE, primary_key=True)
