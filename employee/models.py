from django.db import models




class Employee(models.Model):
    
    POSITIONS = (
        ('1', 'Agent'),
        ('2', 'Factory worker')
    )
    username = models.CharField(max_length=100)
    contact = models.CharField(max_length=200)
    position = models.CharField(max_length=1, choices=POSITIONS)
    password = models.CharField(max_length=15)
    last_login = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username