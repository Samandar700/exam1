# Generated by Django 5.1.2 on 2024-12-18 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_productimage_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='banners/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
