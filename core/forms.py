from .models import *
from django import forms

class RatingForm(forms.ModelForm):
    
    class Meta:
        model = Rating
        fields = ("restaurant","user","rating")


class RestaurantForm(forms.ModelForm):
    
    class Meta:
        model = Restaurant
        fields = ("name","website","date_started","latitude","longitude", "restaurant_type")

