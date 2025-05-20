from django.db import models
import datetime
from django.contrib.auth.models import User


#restaurant
#user
#Rating


class Restaurant(models.Model):
    class Typechoices(models.TextChoices):
        indian='IN','Indian'
        chinese='CH','Chinese'
        Thai='Th','Thai'
        greek='GR','Greek'
        italian='IT','Italian'
        labanese='LB','Labanese'

    name=models.CharField(max_length=100)
    website=models.URLField(default='')
    date_started=models.DateField()
    latitude=models.FloatField(null=True, blank=True)
    longitude=models.FloatField(null=True, blank=True)
    restaurant_type=models.CharField(max_length=2,choices=Typechoices.choices)



    def __str__(self):
        return self.name
    


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant= models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating= models.PositiveSmallIntegerField()


    def __str__(self):
        return f"name: {self.restaurant} , Rating: {self.rating} by {self.user}"
    

class Sale(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.SET_NULL,null=True)
    income=models.DecimalField(max_digits=8,decimal_places=2)
    date_time=models.DateTimeField()

    def __str__(self):
        return f"name: {self.restaurant} , Sales: {self.income}"


