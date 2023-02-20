from django.shortcuts import render
from client.models import Client, Region, District
from employee.models import Employee, Position
from manifactured_product.models import Product, ManufacturedProduct
from rest_framework.views import APIView
from .serializers import ClientSerializers, RegionSerializers, DistrictSerializers, EmployeeSerializers, PositionSerializers, ProductSerializers, ManufacturedProductSerializers
from rest_framework.response  import Response
from rest_framework import status

class ClientAPIView(APIView):
    """Get all clients"""
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializers(clients, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ClientSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegionAPIView(APIView):
    """Get all regions"""
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionSerializers(regions, many=True)
        return Response(serializer.data)
    

class DistrictAPIView(APIView):
    """Get all districts"""
    def get(self, request):
        districts = District.objects.all()
        serializer = DistrictSerializers(districts, many=True)
        return Response(serializer.data)
    

class EmployeeAPIView(APIView):
    """Get all employees"""
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializers(employees, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class PositionAPIView(APIView):
    """Get all positions"""
    def get(self, request):
        positions = Position.objects.all()
        serializer = PositionSerializers(positions, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PositionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProductAPIView(APIView):
    """Get all products"""
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManufacturedProductsAPIView(APIView):
    """Get all manufactured products"""
    def get(self, request):
        manufactured_products = ManufacturedProduct.objects.all()
        serializer = ManufacturedProductSerializers(manufactured_products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        
        serializer = ManufacturedProductSerializers(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    









