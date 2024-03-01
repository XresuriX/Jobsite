import factory
from faker import Faker
import pytz
from jobs import models
import datetime

fake = Faker()


class JobsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Job

    employer_name = fake.name()
    employer_logo = fake.url()
    employer_website = fake.url()
    employer_company_type = fake.name()
    job_publisher = fake.name()
    job_id = fake.random_int()
    job_employment_type = fake.name()
    job_title = fake.name()
    job_apply_link = fake.url()
    job_apply_is_direct = fake.boolean()
    job_description = fake.paragraph()
    job_is_remote = fake.boolean()
    job_posted_at_datetime_utc = factory.Faker("date_time_this_decade", tzinfo=pytz.utc)
    job_city = fake.name()
    job_state = fake.name()
    job_country = fake.country_code()
    job_benefits = fake.paragraph()
    job_google_link = fake.url()
    job_offer_expiration_datetime_utc = factory.Faker("date_time_this_decade", tzinfo=pytz.utc)
    job_required_experience = factory.Faker("pydict", value_types=[str])
    job_required_skills = fake.name()
    job_required_education = factory.Faker("pydict", value_types=[str])
    job_experience_in_place_of_education = fake.boolean()
    job_min_salary = fake.random_int()
    job_max_salary = fake.random_int()
    job_salary_currency = fake.name()
    job_salary_period = fake.name()
    job_highlights = factory.Faker("pydict", value_types=[str])
    job_posting_language = fake.language_code()
