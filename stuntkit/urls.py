from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_stuntkit, name='view_stuntkit'),
    path('full_stuntkit', views.view_full_stuntkit_detail, name='view_full_stuntkit_detail'),
    path('basic_stuntkit', views.view_basic_stuntkit_detail, name='view_basic_stuntkit_detail')
]