# Generated by Django 5.0.3 on 2024-03-16 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0008_alter_company_table_alter_companylocation_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='company',
            table='ircompany_table',
        ),
        migrations.AlterModelTable(
            name='companylocation',
            table='companylocations_table',
        ),
        migrations.AlterModelTable(
            name='companyprojects',
            table='companyprojects_table',
        ),
        migrations.AlterModelTable(
            name='jobseeker',
            table='jobseeker_table',
        ),
        migrations.AlterModelTable(
            name='project',
            table='jobseekerprojects_table',
        ),
        migrations.AlterModelTable(
            name='skill',
            table='skillss_table',
        ),
    ]
