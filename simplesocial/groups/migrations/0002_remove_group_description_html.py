# Generated by Django 4.1 on 2023-10-10 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description_html',
        ),
    ]
