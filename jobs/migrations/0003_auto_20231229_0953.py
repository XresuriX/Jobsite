# Generated by Django 3.2.16 on 2023-12-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20231223_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_highlights',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_required_education',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_required_experience',
            field=models.TextField(blank=True, null=True),
        ),
    ]
