# Generated by Django 5.1.3 on 2024-12-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0008_catagry_product_catagry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagry',
            name='name',
            field=models.CharField(default=1, max_length=20),
        ),
    ]
