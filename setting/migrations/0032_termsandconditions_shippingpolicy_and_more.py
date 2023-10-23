# Generated by Django 4.2.1 on 2023-07-18 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0031_size_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermsAndConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('setting', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='setting.setting')),
            ],
            options={
                'verbose_name_plural': 'Terms and Conditions',
            },
        ),
        migrations.CreateModel(
            name='ShippingPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('setting', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='setting.setting')),
            ],
            options={
                'verbose_name_plural': 'Shipping Policy',
            },
        ),
        migrations.CreateModel(
            name='ReturnsAndRefundsPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('setting', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='setting.setting')),
            ],
            options={
                'verbose_name_plural': 'Returns and Refunds Policy',
            },
        ),
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('setting', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='setting.setting')),
            ],
            options={
                'verbose_name_plural': 'Privacy Policy',
            },
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('setting', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='setting.setting')),
            ],
            options={
                'verbose_name_plural': 'About Us',
            },
        ),
    ]
