from django.conf.urls import url
from .views import *




urlpatterns = [

    url(r'^$', SearchProductView.as_view(),name = "query"),




]
