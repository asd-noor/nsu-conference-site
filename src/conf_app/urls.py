from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='conf-index'),
    path('something/', views.something, name='conf-something'),
]
