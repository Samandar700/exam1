    # Generated by Django 5.1.2 on 2024-12-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_remove_tags_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='code',
            field=models.CharField(default='#000000', max_length=100),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
