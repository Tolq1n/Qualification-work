from django.urls import path
from .views import ClientAPIView, RegionAPIView, DistrictAPIView, EmployeeAPIView, PositionAPIView, ProductAPIView, ManufacturedProductsAPIView


urlpatterns = [
    path('client/', ClientAPIView.as_view()),
    path('region/', RegionAPIView.as_view()),
    path('district/', DistrictAPIView.as_view()),

    path('employee/', EmployeeAPIView.as_view()),
    path('position/', PositionAPIView.as_view()),

    path('product/', ProductAPIView.as_view()),
    path('manufactured-product/', ManufacturedProductsAPIView.as_view()),
]