from django.shortcuts import render
from .forms import RatingForm, RestaurantForm
from .models import Restaurant,Rating,Sale

def home(request):
    # if request.method == 'POST':
    #     form = RatingForm(request.POST or None)  
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = RatingForm()  # Initialize form for GET requests
    # restaurant= Restaurant.objects.all()
    restaurant= Restaurant.objects.all()
    context = {'restaurant': restaurant}  # Pass the form to the context
    return render(request, 'index.html', context)



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