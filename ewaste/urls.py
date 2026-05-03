from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about_us,name="about_us"),
    path("contact/",views.contact,name="contact_us"),

]
