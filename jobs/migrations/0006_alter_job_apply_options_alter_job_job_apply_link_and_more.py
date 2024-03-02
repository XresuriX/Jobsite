# Generated by Django 5.0.1 on 2024-01-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0005_alter_job_employer_company_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="apply_options",
            field=models.JSONField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_apply_link",
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_benefits",
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_city",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_country",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_employment_type",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_google_link",
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_id",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_state",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_title",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]