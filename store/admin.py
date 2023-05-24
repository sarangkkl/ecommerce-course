from django.contrib import admin
from .models import Product,Category,ProductImage,Variation,VariationItem
# Register your models here.
# create product admin
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

class VariationItemInline(admin.TabularInline):
    model = VariationItem
    extra = 3

class VariationAdmin(admin.ModelAdmin):
    inlines = [VariationItemInline,]
    class Meta:
        model = Variation

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,]
    class Meta:
        model = Product

admin.site.register(Category)
admin.site.register(Variation, VariationAdmin)

admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)
admin.site.register(VariationItem)
