from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    url(r'^sign-in/$', auth_views.login, {'template_name' : 'restoran/sign_in.html'}, name="restoran-sign-in"),
    url(r'^sign-out/$', auth_views.logout,{'next_page': '/' } ,name ='restoran-sign-out'),
    url(r'^restorani/$', views.restaurant_home, name='restoran-home'),
    url(r'^sign-up/$', views.restaurant_sign_up,name ='restoran-sign-up')
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)