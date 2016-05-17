from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_before_login, name='home'),
    url(r'^(?i)login', views.login_user, name='login'),
    url(r'^(?i)home', views.home, name='home'),
    url(r'^(?i)about', views.about, name='about'),
    url(r'^(?i)author', views.author, name='author'),
    url(r'^(?i)logout', views.logout_user, name='logout'),
    url(r'^(?i)register', views.register_user, name='register')
]
