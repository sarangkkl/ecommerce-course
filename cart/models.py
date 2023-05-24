from django.db import models
from django.contrib.auth.models import User
from store.models import Product

# Create your models here.



class FavouriteProducts(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    product         = models.OneToOneField(Product, on_delete=models.CASCADE)
    added_on        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    product         = models.OneToOneField(Product, on_delete=models.CASCADE)
    variations      = models.CharField(max_length=100, null=True, blank=True)
    quantity        = models.IntegerField(default=1)
    cartItemHash    = models.CharField(max_length=100, null=True, blank=True)
    added_on        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_sub_total_with_tax(self):
        return (self.product.get_tax_price() + self.product.price)*self.quantity

    def get_sub_total_without_tax(self):
        return self.product.price*self.quantity

