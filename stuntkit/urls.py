from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_stuntkit, name='view_stuntkit')
]