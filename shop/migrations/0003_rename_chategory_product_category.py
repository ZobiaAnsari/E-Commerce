# Generated by Django 4.2.6 on 2024-03-08 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_chategory_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='chategory',
            new_name='category',
        ),
    ]
