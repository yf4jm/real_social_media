# Generated by Django 3.2.4 on 2024-01-06 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_community'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Hashtag',
        ),
    ]
