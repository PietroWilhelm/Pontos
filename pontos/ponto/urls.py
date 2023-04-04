from django.urls import path 
from . import views

urlpatterns = [
    path('', views.baterponto, name='baterponto' ),
]
