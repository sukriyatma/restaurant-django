from django.urls import path
from . import views

urlpatterns = [
    path('', views.empty),
    path('home/', views.home),
    path('reservation/', views.reservation),
    path('bookings', views.getReservation)
]