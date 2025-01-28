from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    guest = models.IntegerField()
    
    def __str__(self):
        return self.name
    

from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('hot', 'Hot Coffee'),
        ('cold', 'Cold Coffee'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='menu_images/')
    
    def __str__(self):
        return self.name
