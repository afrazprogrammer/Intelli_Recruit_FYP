# Generated by Django 5.0.3 on 2024-03-11 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_jobs_loc_jobs_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='slug',
        ),
    ]
