from django.urls import path
from . import views

urlpatterns = [
    #path('', views.app_test),
    path('list/', views.list, name='list'),
    path('create/', views.createPost, name='create'),
    path('detail/<id>/', views.detail, name='detail'),
]