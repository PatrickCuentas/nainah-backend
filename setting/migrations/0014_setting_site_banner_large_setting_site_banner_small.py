# Generated by Django 4.2.1 on 2023-06-28 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0013_rename_shipping_charge_shippingcharge_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='site_banner_large',
            field=models.ImageField(default=1, upload_to='images/site/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='site_banner_small',
            field=models.ImageField(default=1, upload_to='images/site/'),
            preserve_default=False,
        ),
    ]