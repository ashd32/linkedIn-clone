from django.db import models
from locations.models import Country, City


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="companies_logo")
    about = models.TextField()

    def __str__(self):
        return self.name


class Office(models.Model):
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, related_name='offices')
    city = models.ForeignKey(to=City, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(blank=True, upload_to="offices_photos")
    
    def __str__(self):
        return self.company.name