# Generated by Django 3.0.1 on 2020-02-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0033_auto_20200210_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='display',
            field=models.IntegerField(default=1),
        ),
    ]
