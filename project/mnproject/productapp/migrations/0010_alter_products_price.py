# Generated by Django 3.2.5 on 2021-07-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0009_alter_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]