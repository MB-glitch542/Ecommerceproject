# Generated by Django 5.0.2 on 2024-12-07 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakerapp', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]