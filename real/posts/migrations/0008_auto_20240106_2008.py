# Generated by Django 3.2.4 on 2024-01-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_hashtag_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Tags',
            new_name='hashags',
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
