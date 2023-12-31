# Generated by Django 4.2.1 on 2023-06-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0053_delete_variante_delete_varianttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='Select tags for this product', to='product.tag'),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='stock',
            field=models.PositiveBigIntegerField(default=1, help_text='Stock of this variant'),
        ),
    ]
