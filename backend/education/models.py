from django.db import models
from django.contrib.auth import get_user_model
from locations.models import City, Country


User = get_user_model()


class Place(models.Model):
    title = models.CharField(max_lenght=200)
    city = models.ForeignKey(to=City, on_delete=models.SET_NULL, null=True)


class UserEducation(models.Model):
    place = models.ForeignKey(to=Place, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    graduation_date = models.DateField()
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, 
        related_name="educations"
    )
