# Generated by Django 4.2.1 on 2023-06-22 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0028_orderitem_variant_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_charge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
