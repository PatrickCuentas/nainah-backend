# Generated by Django 4.2.1 on 2023-06-29 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0020_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='currency_code',
            field=models.CharField(blank=True, help_text='Enter currency code. Example: USD, EUR, GBP, etc.', max_length=3, null=True),
        ),
    ]
