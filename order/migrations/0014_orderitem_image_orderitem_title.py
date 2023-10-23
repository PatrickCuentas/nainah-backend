# Generated by Django 4.2.1 on 2023-06-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_alter_orderitem_order_alter_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]