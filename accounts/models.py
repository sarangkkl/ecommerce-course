from django.db import models
from django.contrib.auth.models import User
# from store.models import Product

# Create your models here.

class Customer(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name       = models.CharField(max_length=100, null=True, blank=True)
    primary_phone   = models.CharField(max_length=20, null=True, blank=True)
    joined_on       = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Address(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1  = models.CharField(max_length=100)
    address_line_2  = models.CharField(max_length=100, null=True, blank=True)
    city            = models.CharField(max_length=50)
    state           = models.CharField(max_length=50)
    country         = models.CharField(max_length=50)
    postal_code     = models.CharField(max_length=10)
    phone           = models.CharField(max_length=20)
    address_type    = models.CharField(max_length=10, choices=(('billing', 'Billing'), ('shipping', 'Shipping')))
    default         = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


