from . import views
from django.urls import path


urlpatterns = [
    path('<slug:slug>',views.get_product_detail,name='product_detail'),
]