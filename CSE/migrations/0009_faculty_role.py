# Generated by Django 4.1.4 on 2023-01-20 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0008_alter_conference_conference_article_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='role',
            field=models.CharField(choices=[('HOD', 'HOD'), ('OTHER', 'OTHER')], default='OTHER', max_length=10),
        ),
    ]