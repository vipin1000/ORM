from .views import *
from django.urls import path




urlpatterns = [
    path('', home, name='home'),
    path('rest/', add_restaurant , name='add_restaurant')
]
