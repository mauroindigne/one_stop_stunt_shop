from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_tips_advice, name='view_tips_advice'),

]