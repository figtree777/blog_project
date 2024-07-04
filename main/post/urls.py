from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_test),
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
]