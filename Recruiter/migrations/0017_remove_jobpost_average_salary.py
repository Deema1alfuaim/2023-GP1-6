# Generated by Django 4.2.1 on 2023-06-07 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recruiter', '0016_jobpost_average_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='average_salary',
        ),
    ]
