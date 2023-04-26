from django.urls import path
from .views import loginpage, login, logoutuser


urlpatterns = [
    path('', loginpage, name='loginpage'),
    path('login', login, name='login'),
    path('logoutuser', logoutuser, name='logoutuser'),  
]