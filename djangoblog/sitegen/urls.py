from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('resume', views.resume),
    path('about', views.about)
]