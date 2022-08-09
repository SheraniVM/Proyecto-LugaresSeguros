from multiprocessing.spawn import import_main_path
from django.urls import path
from initial import views

urlpatterns = [
    path('Saludos', views.HelloDrf.as_view(), name='index'),
]