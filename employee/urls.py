from django.urls import path
from .views import loginuser, login


urlpatterns = [
    path('', loginuser, name='loginuser'),
    path('login', login, name='login')  
]