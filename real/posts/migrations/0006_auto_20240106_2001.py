# Generated by Django 3.2.4 on 2024-01-06 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20240106_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]