# Generated by Django 4.2.3 on 2023-07-24 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Product_brand',
            new_name='product_brand',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_pic',
            new_name='product_pic',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_price',
            new_name='product_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_size',
            new_name='product_size',
        ),
    ]
