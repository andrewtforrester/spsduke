# Generated by Django 3.0.1 on 2020-02-15 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0036_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
