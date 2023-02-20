from rest_framework import serializers
from client.models import Client, Region, District
from employee.models import Employee, Position
from manifactured_product.models import Product, ManufacturedProduct

class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class DistrictSerializers(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class PositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ManufacturedProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = ManufacturedProduct
        fields = '__all__'
