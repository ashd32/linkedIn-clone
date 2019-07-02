from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE, 
        related_name="cities"
    )

    def __str__(self):
        return self.name