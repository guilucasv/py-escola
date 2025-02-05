from django.contrib import admin
from django.urls import path
from escola import views


app_name = 'escola'


urlpatterns = [
    path('', views.index, name='index'),
]