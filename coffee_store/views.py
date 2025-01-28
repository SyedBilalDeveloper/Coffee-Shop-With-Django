from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Booking

def booking(request):
    if request.method == "POST":
        # Manually extract data from POST request
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        guest = request.POST.get("person")

        # Validate data
        if not all([name, email, phone, date, time, guest]):
            messages.error(request, "All fields are required.")
        else:
            try:
                # Save data to the database
                booking = Booking(name=name, email=email, phone=phone, date=date, time=time, guest=guest)
                booking.save()
                # Display success message and stay on the page
                messages.success(request, "Booking successful!")

            except Exception as e:
                messages.error(request, f"An error occurred: {e}")

        # Render the same page with messages (for both success and error)
        # return render(request, "coffee_store/index.html")

    # Render the page for a GET request
    return render(request, "coffee_store/index.html")


def contact(request):
    # return HttpResponse("Contact us at coffee@store.com.")
    return render(request, "coffee_store/contact.html")

# Create your views here.

def shop(request):
    return HttpResponse("Shop is our menu.")

def about(request):
    return render(request, 'coffee_store/about.html')


def home(request):
    hot_coffee_items = MenuItem.objects.filter(category='hot')
    cold_coffee_items = MenuItem.objects.filter(category='cold')
    
    context = {
        'hot_coffee_items': hot_coffee_items,
        'cold_coffee_items': cold_coffee_items
    }
    return render(request, 'coffee_store/index.html', context)
    


def service(request):
        return render(request, 'coffee_store/service.html')

def gallery(request):
        return render(request, 'coffee_store/gallery.html')

from django.shortcuts import render
from .models import MenuItem

# def menu(request):
#         return render(request, '')

def menu(request):
    hot_coffee_items = MenuItem.objects.filter(category='hot')
    cold_coffee_items = MenuItem.objects.filter(category='cold')
    
    context = {
        'hot_coffee_items': hot_coffee_items,
        'cold_coffee_items': cold_coffee_items
    }
    
    return render(request, 'coffee_store/menu.html', context)
