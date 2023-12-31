# Generated by Django 4.2.1 on 2023-06-13 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0002_setting_site_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('social_facebook', models.CharField(max_length=100)),
                ('social_instagram', models.CharField(max_length=100)),
                ('social_tiktok', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='setting',
            name='site_description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='site_favicon',
            field=models.ImageField(default=1, upload_to='images/site/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='site_icon',
            field=models.ImageField(default=1, upload_to='images/site/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='site_keywords',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='site_logo',
            field=models.ImageField(default=1, upload_to='images/site/'),
            preserve_default=False,
        ),
    ]
