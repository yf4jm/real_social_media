# Generated by Django 3.2.4 on 2024-01-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='total_contribution_power',
            field=models.FloatField(default=0.0),
        ),
    ]
