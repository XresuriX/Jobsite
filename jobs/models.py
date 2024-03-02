from django.db import models
from django.urls import reverse


class EntrylvlManager(models.Manager):
    # manger for filtering for entry level jobs
    def get_queryset(self):
        return super().get_queryset().filter(job_title="entry level")


class Job(models.Model):
    employer_name = models.CharField(max_length=400, blank=True, null=True)
    employer_logo = models.URLField(max_length=400, blank=True, null=True)
    employer_website = models.URLField(max_length=400, blank=True, null=True)
    employer_company_type = models.CharField(max_length=400, blank=True, null=True)
    job_publisher = models.CharField(max_length=400, blank=True, null=True)
    job_id = models.CharField(max_length=400, blank=True, null=True)
    job_employment_type = models.CharField(max_length=400, blank=True, null=True)
    job_title = models.CharField(max_length=400, blank=True, null=True)
    job_apply_link = models.URLField(max_length=400, blank=True, null=True)
    apply_options = models.JSONField(max_length=400, blank=True, null=True)
    job_apply_is_direct = models.BooleanField(blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    job_is_remote = models.BooleanField(blank=True, null=True)
    job_posted_at_datetime_utc = models.DateTimeField(max_length=30, blank=True, null=True)
    job_city = models.CharField(max_length=400, blank=True, null=True)
    job_state = models.CharField(max_length=400, blank=True, null=True)
    job_country = models.CharField(max_length=400, blank=True, null=True)
    job_benefits = models.CharField(max_length=4000, blank=True, null=True)
    job_google_link = models.URLField(max_length=400, blank=True, null=True)
    job_offer_expiration_datetime_utc = models.DateTimeField(
        max_length=30, blank=True, null=True
    )
    job_required_skills = models.TextField(max_length=2000, blank=True, null=True)
    job_experience_in_place_of_education = models.BooleanField(blank=True, null=True)
    job_min_salary = models.FloatField(null=True, max_length=30, blank=True, )
    job_max_salary = models.FloatField(null=True, max_length=30, blank=True )
    job_salary_currency = models.CharField(max_length=200, blank=True, null=True)
    job_salary_period = models.CharField(max_length=200, blank=True, null=True)
    
    job_posting_language = models.CharField(max_length=5, blank=True, null=True)
    job_required_experience = models.JSONField(null=True, blank=True)
    job_required_education = models.JSONField(null=True, blank=True)
    job_highlights = models.JSONField(null=True, blank=True)

    def __str__(self):
        return "{} /by {}/is remote? {}/posted {}".format(
            self.job_title,
            self.employer_name,
            self.job_is_remote,
            self.job_posted_at_datetime_utc,
        )

    def get_absolute_url(self):
        return reverse('details', args=[str(self.pk)])
    
    objects = models.Manager()
    entrylevel = EntrylvlManager()

""""""