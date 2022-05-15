from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=500)
    author=models.CharField(max_length=255,null=True,blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])