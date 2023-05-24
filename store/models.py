from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import Customer
# Create your models here

class Category(models.Model):
    name            = models.CharField(max_length=100)
    description     = RichTextField(max_length=100)
    slug            = models.SlugField(max_length=100,blank=True,null=True)
    image           = models.ImageField(upload_to='uploads/category/', null=True, blank=True)

    def __str__(self):
        return self.name

TAX_CHOICES = (
    ('0.05', '5%'),
    ('0.10', '10%'),
    ('0.15', '15%'),
    ('0.18', '18%'),
    ('0.22', '22%'),
)
MEDIA_TYPE = (
    ('image', 'Image'),
    ('video', 'Video'),

)

class Product(models.Model):
    name            = models.CharField(max_length=100)
    slug            = models.SlugField(max_length=100,blank=True,null=True)
    small_desc      = models.CharField(max_length=255)
    description     = RichTextField(max_length=2000)
    image           = models.ImageField(upload_to='uploads/product/', null=True, blank=True)
    market_price    = models.DecimalField(max_digits=10,decimal_places=2)
    category        = models.ManyToManyField(Category, related_name='products')
    our_price       = models.DecimalField(max_digits=10,decimal_places=2)
    stock           = models.IntegerField(default=1)
    tax             = models.CharField(max_length=10, choices=TAX_CHOICES, default='0.05')
    is_on_sale      = models.BooleanField(default=False)
    is_featured     = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


    def get_images(self):
        return ProductImage.objects.filter(product=self)

    def get_variations(self):
        return Variation.objects.filter(product=self)

    def get_tax_price(self):
        return self.our_price * float(self.tax)
    
    def get_discount_percent(self):
        return int(100 - (self.our_price * 100 / self.market_price))


class ProductImage(models.Model):
    product         = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    type            = models.CharField(max_length=10, choices=MEDIA_TYPE, default='image')
    image           = models.ImageField(upload_to='uploads/product/', null=True, blank=True)

    def __str__(self):
        return self.product.name


class Variation(models.Model):
    name           = models.CharField(max_length=100)
    product        = models.ForeignKey(Product, related_name='variations', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_variation_value(self):
        return VariationItem.objects.filter(variation=self)


class VariationItem(models.Model):
    variation      = models.ForeignKey(Variation, related_name='items', on_delete=models.CASCADE)
    value          = models.CharField(max_length=100)


class Review(models.Model):
    product         = models.OneToOneField(Product, related_name='reviews', on_delete=models.CASCADE)
    customer        = models.OneToOneField(Customer, related_name='reviews', on_delete=models.CASCADE)
    review          = models.TextField()
    rating          = models.DecimalField(max_digits=2,decimal_places=1)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name





