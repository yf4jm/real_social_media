# Generated by Django 3.2.4 on 2024-01-17 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_created_on'),
        ('posts', '0024_contribution_power'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='like',
            new_name='PostLike',
        ),
    ]
