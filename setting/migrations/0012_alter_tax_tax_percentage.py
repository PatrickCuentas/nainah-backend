# Generated by Django 4.2.1 on 2023-06-20 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0011_shippingcharge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax',
            name='tax_percentage',
            field=models.DecimalField(blank=True, decimal_places=4, help_text='Enter tax percentage in decimal format. Example: 0.05 for 5% tax.', max_digits=10, null=True),
        ),
    ]
