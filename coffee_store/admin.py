from django.contrib import admin
from .models import Booking, MenuItem

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'guest')
      

admin.site.register(Booking, BookingAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'image')
    

admin.site.register(MenuItem, MenuAdmin)