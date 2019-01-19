"""bookmyplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from products.views import *
from mytab.views import *
from .views import *
from posts.views import *




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^contact/$', contact_page, name="contact"),
    url(r'^login/$', login_page, name="login"),
    url(r'^restoran/', include('restoran1.urls', namespace='restorani')),
    url(r'^register/$', register_page, name="register"),
    url(r'^about/$', about_page, name = "about"),
    url(r'^products/', include("products.urls", namespace = "products")),
    url(r'^search/', include("search.urls", namespace = "search")),
    url(r'^tab/$', tab_home, name='tab'),
    url(r'^posts/', include("posts.urls", namespace = "posts")),
    #url(r'^locali/', include("bar_rest_club.urls", namespace = 'objects')),
    url(r'^api/posts/', include("posts.api.urls", namespace = "posts-api")),
]

#   
if settings.DEBUG: #to verify still STATIC
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
