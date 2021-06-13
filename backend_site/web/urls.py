from django.urls import path
from . import views

urlpatterns = [
    path('api/cars/', views.CarView.as_view()),
]