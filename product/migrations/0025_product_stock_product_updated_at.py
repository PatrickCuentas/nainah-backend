# Generated by Django 4.2.1 on 2023-06-13 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_productvariant_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]