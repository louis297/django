from django.db import models


class CountryModel(models.Model):
    country_name = models.CharField(max_length=40)
    country_abbr = models.CharField(max_length=2)
    activate = models.BooleanField(default=True)


class StateModel(models.Model):
    state_name = models.CharField(max_length=40)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    activate = models.BooleanField(default=True)


class CityModel(models.Model):
    city_name = models.CharField(max_length=40)
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE)
    activate = models.BooleanField(default=True)
