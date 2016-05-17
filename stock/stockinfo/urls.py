'''Urls for the Stockinfo app'''
from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^(?i)stockinfo', views.stockinfo, name="stockinfo"),
    url(r'^(?i)search', views.getstock, name="getstock"),
    url(r'^(?i)add', views.addstock, name="addstock"),
]
