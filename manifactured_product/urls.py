from django.urls import path
from .views import manufacturedmroduct, add_mproduct, show_mproduct


urlpatterns = [
    path('', manufacturedmroduct, name='manufacturedmroduct'),
    path('add_mproduct', add_mproduct, name='add_mproduct'),
    path('show_mproduct', show_mproduct, name='show_mproduct'),
]