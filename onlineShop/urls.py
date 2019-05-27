from django.urls import path
from onlineShop import views

#Url routes are case sensitive
urlpatterns = [
    path("", views.home, name="home"),
]