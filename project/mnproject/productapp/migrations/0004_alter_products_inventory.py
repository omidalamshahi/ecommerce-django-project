# Generated by Django 3.2.5 on 2021-07-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_products_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='inventory',
            field=models.IntegerField(default=1),
        ),
    ]
