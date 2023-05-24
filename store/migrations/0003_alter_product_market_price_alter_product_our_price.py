# Generated by Django 4.2 on 2023-05-08 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_slug_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='market_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='our_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]