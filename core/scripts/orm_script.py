from core.models import *
from django.utils import timezone
from django.db import connection
from pprint import pprint
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
    #     name="VEGI's",
    #     date_started= timezone.now(),
    #     latitude=78.69,
    #     longitude=78.69,
    #     restaurant_type=Restaurant.Typechoices.italian

    # ) 
    # restaurant=Restaurant.objects.all()
    # for restaurant in restaurant:  # Iterate over each restaurant
    #     ratings = restaurant.rating_set.all()  # Access the related ratings for the restaurant
    #     pprint(f"Ratings for {restaurant.name}: {ratings}")
    # rating=Rating.objects.count()
    # sale=Sale.objects.count()
    # user=User.objects.count()
    # print(user)
    # pprint(ratings)
    # print(rating
    # print(sale)
    
    # rating= Rating.objects.filter(rating=6).delete(
        
        # )
    


    # print(rating)

   
    # Rating.objects.create(user=user, restaurant=restaurant, rating=6)
    # rating=Rating(user=user, restaurant=restaurant, rating=5)
    # rating.full_clean()
    # rating.save()


    
    # Restaurant.name=a
    # Restaurant.save()


    # pprint(connection.queries)


    staff,created=Staff.objects.get_or_create(name="jhony")
    # print(staff.restaurant.all())
    staff.restaurant.add(Restaurant.objects.all()[6])
    staff.restaurant.set(Restaurant.objects.all()[0:6])
    # print(staff.restaurant.clear())
    print(staff.restaurant.count())

    

