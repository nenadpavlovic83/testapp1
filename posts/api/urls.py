from django.conf.urls import url

from django.views.generic.base import RedirectView
from .views import * 

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name = 'search'),
    # url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name = 'detail'),
    # url(r'^$', PostListView.as_view(), name = 'list'),
    # url(r'^(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name = 'update'),
    # url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name = 'delete'),
  
]
