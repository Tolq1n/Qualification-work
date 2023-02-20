from django.db import models

# Create your models here.



class Client(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    district = models.ForeignKey('District', on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
