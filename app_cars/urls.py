from django.urls import path
from app_cars import views

app_name = 'app_cars'

urlpatterns = [
    path('', views.index, name='index'),

]