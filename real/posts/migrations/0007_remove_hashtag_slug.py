# Generated by Django 3.2.4 on 2024-01-06 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20240106_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtag',
            name='slug',
        ),
    ]
