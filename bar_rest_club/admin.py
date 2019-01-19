from django.contrib import admin
from .models import RestaurantReview, Restaurant, Dish

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(RestaurantReview)