from django.shortcuts import render
from .forms import RatingForm, RestaurantForm
from .models import Restaurant,Rating,Sale,StaffRestaurant

def home(request):
    # if request.method == 'POST':
    #     form = RatingForm(request.POST or None)  
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = RatingForm()  # Initialize form for GET requests
    # restaurant= Restaurant.objects.all()
    # restaurant= Restaurant.objects.all()
      # Pass the form to the context
    rests=StaffRestaurant.objects.prefetch_related('staff','restaurants')
    context={"rest":rests}
    return render(request, 'index.html',context=context)



def add_restaurant(request):
    # if request.method=='POST':
    #     form = RestaurantForm(request.POST or None)
    #     if form.is_valid ():
    #         form.save()
    # else :
    #     form =  RestaurantForm()
    rating=Rating.objects.only('rating','restaurant__name').select_related('restaurant')
    context= {'rating':rating}
    return render (request, 'add_rest.html',context)         