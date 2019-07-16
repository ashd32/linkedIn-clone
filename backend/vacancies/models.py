from django.db import models
from django.contrib.auth import get_user_model
from companies.models import Company


User = get_user_model()


class Vacancy(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    description = models.TextField(verbose_name="description")
    position = models.CharField(verbose_name="position", max_length=150)
    company = models.ForeignKey(
        to=Company, 
        on_delete=models.CASCADE,
        verbose_name="company",
        related_name="vacancies"
    )
    publish_date = models.DateField(auto_add_now=True, verbose_name="publish date")
    update_date = models.DateField(auto_add_now=True, verbose_name="last update")
    
    def __str__(self):
        return self.title

    
class Experience(models.Model):
    user = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        related_name='experiences')
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    finish_data = models.DateField(blank=True)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    about = models.TextField()


    def __str__(self):
        return self.position


