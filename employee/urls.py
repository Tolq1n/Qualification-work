from django.urls import path
from .views import loginuser, login, logoutuser


urlpatterns = [
    path('', loginuser, name='loginuser'),
    path('login', login, name='login'),
    path('logout', logoutuser, name='logout'),  
]