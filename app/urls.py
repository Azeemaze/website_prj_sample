from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('About/', views.About, name='About'),
    path('Service/', views.Service, name='Service'),
    path('Contact/', views.Contact, name='Contact'),
    path('price/', views.price, name='price'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('appointment/', views.appointment, name='appointment'),

]