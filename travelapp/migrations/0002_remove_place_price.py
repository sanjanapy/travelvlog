# Generated by Django 3.2.16 on 2023-01-13 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='price',
        ),
    ]
