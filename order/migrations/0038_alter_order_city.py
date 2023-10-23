# Generated by Django 4.2.1 on 2023-06-30 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0024_delete_shippingcharge'),
        ('order', '0037_alter_order_city_alter_order_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.ForeignKey(help_text='Select City.', on_delete=django.db.models.deletion.PROTECT, to='setting.tax'),
        ),
    ]
