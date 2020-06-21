
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('ee/', views.another, name='another'),
    path('dd/', views.ann, name='ann'),
]