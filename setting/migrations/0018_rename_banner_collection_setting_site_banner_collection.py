# Generated by Django 4.2.1 on 2023-06-28 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0017_setting_banner_collection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='banner_collection',
            new_name='site_banner_collection',
        ),
    ]