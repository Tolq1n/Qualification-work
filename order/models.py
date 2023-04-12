from django.db import models
from client.models import Client
from employee.models import Employee    
from manifactured_product.models import Product



class Order(models.Model):
    CURRENCY = (("UZS", "UZS"), ("RUB", "RUB"), ("USD", "USD") )
    PAYMENT = (("CASH", "CASH"), ("BANK CARD", "BANK CARD"), ("TRANSFER", "TRANSFER"))       

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.CharField(max_length=30)
    amount_order = models.FloatField()
    total_price = models.FloatField()
    discount = models.FloatField(default=0)
    total_discount = models.FloatField(default=0)
    total_price_with_discaunt = models.FloatField()
    currency = models.CharField(max_length=9, choices=CURRENCY)
    payment_type = models.CharField(max_length=9, choices = PAYMENT)



    def __str__(self):
        return f"{self.client.name}   {self.client.district}    {self.client.contact}"

# class ProductOrder(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     amount_order = models.FloatField()
#     unit_price = models.CharField(max_length=30)
#     total_price = models.FloatField()
#     total_discount = models.FloatField()
#     discount = models.FloatField()

#     def __str__(self):
#         return self.product.name
