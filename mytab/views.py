from django.shortcuts import render
from .models import *
# # Create your views here.
#
# def tab_create(user=None):
#     tab_obj = Tab.objects.create(user=None)
#     print("new Tab Created!")
#     return tab_obj

def tab_home(request):
    tab_obj, new_obj = Tab.objects.new_or_get(request)
    products = tab_obj.products.all()
    total = 0
    for i in products:
        total += i.price
    print(total)
    tab_obj.total = total
    tab_obj.save()
    return render(request, "tabs/home.html", {})
