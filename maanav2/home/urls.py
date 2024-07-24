from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/contact/', views.postcontact, name='postcontact'),
    path('man/',views.man , name = 'man'),
]
