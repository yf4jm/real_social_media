# Generated by Django 3.2.4 on 2024-01-17 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_auto_20240117_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='power',
            field=models.FloatField(default=0.0),
        ),
    ]