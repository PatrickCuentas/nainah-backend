# Generated by Django 4.2.1 on 2023-06-20 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_orderitem_price_sell'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='price_sell',
            new_name='price',
        ),
    ]
