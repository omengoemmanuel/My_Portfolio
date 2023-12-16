from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact"),
    path('work', views.work, name="work"),
    path('sendmessage', views.sendmessage, name ="sendmessage")



]
