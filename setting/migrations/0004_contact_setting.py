# Generated by Django 4.2.1 on 2023-06-13 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0003_contact_setting_site_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='setting',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='setting.setting'),
            preserve_default=False,
        ),
    ]
