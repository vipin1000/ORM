from core.models import *
from django.utils import timezone
from django.db import connection
from pprint import pprint
import random
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
    
    # delete= StaffRestaurant.objects.filter(id=8).delete()
    


    # print(rating)

   
    # Rating.objects.create(user=user, restaurant=restaurant, rating=6)
    # rating=Rating(user=user, restaurant=restaurant, rating=5)
    # rating.full_clean()
    # rating.save()


    
    # Restaurant.name=a
    # Restaurant.save()


    # pprint(connection.queries)


    staff,created=Staff.objects.get_or_create(name="jack")

    staff.restaurants.set(Restaurant.objects.all()[:10],
                        through_defaults= {'salary':random.randint(20000,50000)})
    # print(staff)
    # print(created)
    
    # restaurant1=Restaurant.objects.all()[2]
    # print(restaurant1)
   
    # restaurant2=Restaurant.objects.all()[3]
    # print(restaurant2)

    # StaffRestaurant.objects.create(
    #     staff=staff,
    #     restaurant=restaurant1,
    #     salary=28000)
    

    # StaffRestaurant.objects.create(
    #     staff=staff,
    #     restaurant=restaurant2,
    #     salary=20000)
    # # staff.restaurant.add(Restaurant.objects.all()[6])
    # staff.restaurant.set(Restaurant.objects.all()[0:11:2])
    # # print(staff.restaurant.clear())
    # print(staff.restaurant.count())

    # rest=Restaurant.objects.get(pk=24)
    # print(rest.website)
    # print(rest.staff_set.all())
    # print(rest.website)
   
    

