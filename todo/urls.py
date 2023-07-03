from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
]