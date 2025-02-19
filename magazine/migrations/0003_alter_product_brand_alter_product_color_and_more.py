# Generated by Django 5.1.3 on 2025-01-13 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_shoppingcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='magazine.brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, to='magazine.color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, to='magazine.size'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='magazine.tags'),
        ),
    ]
