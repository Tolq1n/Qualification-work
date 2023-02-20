from django.urls import path
from .views import create_client, show_clients, add_client

urlpatterns = [
    path('', create_client, name='create_client'),
    path('show_clients', show_clients, name='show_clients'),
    path('add_client', add_client, name='add_client'),
]