# Generated by Django 5.1.3 on 2024-12-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0010_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
