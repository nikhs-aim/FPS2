# Generated by Django 4.1.4 on 2023-01-17 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0002_alter_faculty_age_journal_conference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='role',
        ),
    ]
