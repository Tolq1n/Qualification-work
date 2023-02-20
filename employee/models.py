from django.db import models




class Employee(models.Model):
    username = models.CharField(max_length=100)
    contact = models.CharField(max_length=200)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    password = models.CharField(max_length=15)
    def __str__(self):
        return self.username

class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name