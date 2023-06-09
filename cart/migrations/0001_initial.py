# Generated by Django 4.2 on 2023-05-14 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_product_stock_product_tax_productimage_type_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variations', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('cartItemHash', models.CharField(blank=True, max_length=100, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
