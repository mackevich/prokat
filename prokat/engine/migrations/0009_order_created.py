# Generated by Django 2.1.2 on 2018-11-03 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0008_auto_20181025_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]