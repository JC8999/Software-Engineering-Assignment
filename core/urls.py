from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('practice-areas/', views.practice_areas, name='practice_areas'),
]