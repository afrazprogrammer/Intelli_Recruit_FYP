# Generated by Django 5.0.3 on 2024-03-11 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_remove_jobs_is_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='post',
            field=models.CharField(max_length=2551),
        ),
    ]