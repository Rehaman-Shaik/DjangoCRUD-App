from django.urls import path
from . import views

urlpatterns = [
    path('series/', views.series_home, name = 'series_home'),
]