from django.urls import path
from .views import add_order, orders


urlpatterns = [
    path('', add_order, name='addorder'),
    path('orders/', orders, name = 'orders'),
      
]