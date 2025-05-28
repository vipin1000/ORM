from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.core import validators

#restaurant
#user
#Rating

def name_strt_with_a(x):
    if not x.startswith('a'):
        raise ValidationError("Name must start with letter a")


class Restaurant(models.Model):
    class Typechoices(models.TextChoices):
        indian='IN','Indian'
        chinese='CH','Chinese'
        Thai='Th','Thai'
        greek='GR','Greek'
        italian='IT','Italian'
        labanese='LB','Labanese'

    name=models.CharField(max_length=100, validators=[name_strt_with_a])
    website=models.URLField(null=True, blank=True)
    date_started=models.DateField()
    latitude=models.FloatField(null=True, blank=True,validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude=models.FloatField(null=True, blank=True, validators=[MinValueValidator(-180), MaxValueValidator(180)])
    restaurant_type=models.CharField(max_length=2,choices=Typechoices.choices)

    def __str__(self):
        return self.name
    



class Staff(models.Model):
    name=models.CharField(max_length=200)
    restaurant=models.ManyToManyField(Restaurant)
    def __str__(self):
        restaurant_names = ", ".join([restaurant.name for restaurant in self.restaurant.all()])
        return f"{self.name} ------ {restaurant_names}"





class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant= models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    rating= models.PositiveSmallIntegerField(validators= [MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"name: {self.restaurant} , Rating: {self.rating} by {self.user}"
    

class Sale(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.SET_NULL,null=True,related_name='sales')
    income=models.DecimalField(max_digits=8,decimal_places=2)
    date_time=models.DateTimeField()

    def __str__(self):
        return f"name: {self.restaurant} , Sales: {self.income}"


