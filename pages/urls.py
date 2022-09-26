
from django.urls import path
from.import views

urlpatterns=[
    path('', views.home, name='home'),
    path('available/',views.available, name='available'),
    path('seat/', views.seat, name='seat'),
    path('sigup/',views.sigup, name='sigup'),
    path('signin/', views.signin, name='signin')


]