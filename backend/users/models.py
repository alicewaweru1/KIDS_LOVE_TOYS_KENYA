from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user model for Kids Love Toys.
    
    Customers can create accounts and place orders, while admins\owners can manage the products
    
    """
    
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    address = models.TextField(blank=True, null=True)
    
    is_customer = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username
