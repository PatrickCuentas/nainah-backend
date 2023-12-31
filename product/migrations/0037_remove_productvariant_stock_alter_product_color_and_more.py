# Generated by Django 4.2.1 on 2023-06-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0036_product_color_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariant',
            name='stock',
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, choices=[('Black', 'Black'), ('White', 'White'), ('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Purple', 'Purple'), ('Pink', 'Pink'), ('Brown', 'Brown'), ('Grey', 'Grey'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Beige', 'Beige'), ('Bronze', 'Bronze'), ('Copper', 'Copper'), ('Clear', 'Clear'), ('Cream', 'Cream'), ('Multi', 'Multi'), ('Navy', 'Navy'), ('Tan', 'Tan'), ('Turquoise', 'Turquoise'), ('Other', 'Other')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('5', '5'), ('5.5', '5.5'), ('6', '6'), ('6.5', '6.5'), ('7', '7'), ('7.5', '7.5'), ('8', '8'), ('8.5', '8.5'), ('9', '9'), ('9.5', '9.5'), ('10', '10'), ('11', '11'), ('11.5', '11.5'), ('12', '12'), ('12.5', '12.5'), ('13', '13'), ('13.5', '13.5'), ('14', '14'), ('14.5', '14.5'), ('15', '15')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='color',
            field=models.CharField(blank=True, choices=[('Black', 'Black'), ('White', 'White'), ('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Purple', 'Purple'), ('Pink', 'Pink'), ('Brown', 'Brown'), ('Grey', 'Grey'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Beige', 'Beige'), ('Bronze', 'Bronze'), ('Copper', 'Copper'), ('Clear', 'Clear'), ('Cream', 'Cream'), ('Multi', 'Multi'), ('Navy', 'Navy'), ('Tan', 'Tan'), ('Turquoise', 'Turquoise'), ('Other', 'Other')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='size',
            field=models.CharField(blank=True, choices=[('5', '5'), ('5.5', '5.5'), ('6', '6'), ('6.5', '6.5'), ('7', '7'), ('7.5', '7.5'), ('8', '8'), ('8.5', '8.5'), ('9', '9'), ('9.5', '9.5'), ('10', '10'), ('11', '11'), ('11.5', '11.5'), ('12', '12'), ('12.5', '12.5'), ('13', '13'), ('13.5', '13.5'), ('14', '14'), ('14.5', '14.5'), ('15', '15')], max_length=100, null=True),
        ),
    ]
