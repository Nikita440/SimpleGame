from django.db import models
from django.contrib.auth.models import User



class UserInfo(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=20,default="Anonymus")
    role = models.CharField(max_length=20,default = "Buyer")
    balance = models.PositiveIntegerField(default = 0)
    level = models.PositiveIntegerField(default = 0)
    purchises = models.PositiveIntegerField(default = 0)
    
class Shop(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    rating = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Position(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    amount = models.IntegerField()
    type = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.TextField()
    place = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type} at {self.place}"