# Generated by Django 4.2.1 on 2023-06-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='show_quantity',
            field=models.PositiveIntegerField(default=8, help_text='Show quantity of products in catalog?'),
        ),
    ]
