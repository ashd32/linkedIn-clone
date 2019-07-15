from django.db import models


class Country(models.Model):
    country_id = models.CharField(primary_key=True, unique=True, max_length=10)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    city_id = models.CharField(primary_key=True, unique=True, max_length=10)
    name = models.CharField(max_length=200)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE, 
        related_name="cities"
    )
    parent_id = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name