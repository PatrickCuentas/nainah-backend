# Generated by Django 4.2.1 on 2023-06-22 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0049_productvariantattribute_productattribute'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productattribute',
            name='attribute',
        ),
    ]
