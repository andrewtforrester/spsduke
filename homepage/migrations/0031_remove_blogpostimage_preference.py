# Generated by Django 3.0.1 on 2020-02-10 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0030_remove_eventimage_preference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpostimage',
            name='preference',
        ),
    ]
