from core.models import *
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
def run():
    # restaurant=Restaurant()
    # restaurant.name='veer ji'
    # restaurant.date_started= timezone.now()
    # restaurant.latitude=78.69
    # restaurant.longitude=7.36
    # restaurant.restaurant_type=Restaurant.Typechoices.indian

    # restaurant.save()

    # restaurant=Restaurant.objects.first()
    # user=User.objects.first()
    # restaurant=Restaurant.objects.create(
    #     name="Domin",
    #     date_started= timezone.now(),
    #     latitude=78.69,
    #     longitude=78.69,
    #     restaurant_type=Restaurant.Typechoices.italian

    # )

    # rating= Rating.objects.create(
    #     user=user,
    #     restaurant=restaurant,
    #     rating=4)
    


    # print(restaurant)
    # print(user)
    print(Rating.objects.filter(rating=4))

    # print(connection.queries)

    

