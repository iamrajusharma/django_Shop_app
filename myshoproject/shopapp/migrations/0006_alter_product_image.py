# Generated by Django 5.1.3 on 2024-12-03 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='static/images/default_image.jpg', upload_to='static/images/'),
        ),
    ]
