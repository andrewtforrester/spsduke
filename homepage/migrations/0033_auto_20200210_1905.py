# Generated by Django 3.0.1 on 2020-02-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0032_remove_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='date',
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
