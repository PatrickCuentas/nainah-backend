# Generated by Django 4.2.1 on 2023-06-29 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0034_remove_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_option',
            field=models.CharField(choices=[('shipping', 'Shipping'), ('store_pickup', 'Store Pickup'), ('delivery', 'Delivery')], default='shipping', max_length=20),
        ),
    ]
