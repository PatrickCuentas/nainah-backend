# Generated by Django 4.2.1 on 2023-06-30 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_catalog_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalog',
            options={'ordering': ['order'], 'verbose_name': 'Catalog', 'verbose_name_plural': 'Catalogs'},
        ),
        migrations.AddField(
            model_name='catalog',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
