# Generated by Django 3.2.5 on 2021-07-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0008_rename_image_products_product_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
