from django.conf import settings
from django.db import models
from django.db.models.signals import m2m_changed, pre_save, post_save
from products.models import Product
# Create your models here.
User = settings.AUTH_USER_MODEL

class TabManager(models.Manager):

    def new_or_get(self,request):
        tab_id = request.session.get("tab_id", None)
        qs = self.get_queryset().filter(id=tab_id)
        if qs.count()==1:
            new_obj=False
            print("tabID exists!")
            tab_obj = qs.first()
            if request.user.is_authenticated and tab_obj.user is None:
                tab_obj.user = request.user
                tab_obj.save()
        else:
            tab_obj = Tab.objects.new(user=request.user)
            new_obj = True
            request.session['tab_id'] = tab_obj.id

        return tab_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Tab(models.Model):
    user = models.ForeignKey(User, null=True, blank = True)
    #remove null and blank - unauthenticated users
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = TabManager()

    def __str__(self):
        return str(self.id)



def pre_save_tab_receiver(sender, action, instance, *args, **kwargs):
    print(action)
    products = instance.products.all()
    total = 0
    for i in products:
        total += i.price
    print(total)
    instance.total = total

m2m_changed.connect(pre_save_tab_receiver, sender = Tab)
