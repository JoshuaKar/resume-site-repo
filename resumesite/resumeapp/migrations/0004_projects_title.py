# Generated by Django 4.2.4 on 2023-08-23 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0003_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='title',
            field=models.CharField(default='project', max_length=200),
        ),
    ]
