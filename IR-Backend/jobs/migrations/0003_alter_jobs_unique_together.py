# Generated by Django 5.0.3 on 2024-03-11 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_rename_location_jobs_post'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='jobs',
            unique_together={('title', 'company')},
        ),
    ]
