# Generated by Django 2.1.2 on 2018-10-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0004_auto_20181023_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
