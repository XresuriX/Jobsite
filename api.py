from datetime import datetime
import json
import os
import logging
import django
import environ
import requests
from unittest.mock import patch
from decouple import config
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings.local")
django.setup()

env = environ.Env()
environ.Env.read_env()
from jobs.models import Job

from decouple import config


class JobFetcher:
    """
    Job fetch api"""

    def __init__(
        self,
        query,
        pages,
        posted,
    ):
        self.url = "https://jsearch.p.rapidapi.com/search"
        self.headers = {}
        self.Key = config('Key', default='False')

        self.headers = {
            "X-RapidAPI-Key": self.Key,
            "X-RapidAPI-Host": "jsearch.p.rapidapi.com",
        }

    query = input("what are we looking for today? ")
    pages = input("how many pages? Number of pages to return, starting from page. ")
    posted = input("date posted? Allowed values: all, today, 3days, week,month. ")

    def convert_json_strings(self, data):
        data['job_required_experience'] = json.dumps(data['job_required_experience'])
        data['job_required_skills'] = json.dumps(data['job_required_skills'])
        data['job_highlights'] = json.dumps(data['job_highlights'])
        return data

    def create_job_instance(self, job_data):
        job_list = {
            "employer_name":job_data['employer_name'],
            "employer_logo":job_data['employer_logo'],
            "employer_website":job_data['employer_website'],
            "employer_company_type":job_data['employer_company_type'],
            "job_publisher":job_data['job_publisher'],
            "job_id":job_data['job_id'],
            "job_employment_type":job_data['job_employment_type'],
            "job_title":job_data['job_title'],
            "job_apply_link":job_data['job_apply_link'],
            "job_apply_is_direct":job_data['job_apply_is_direct'],
            "job_description":job_data['job_description'],
            "job_is_remote":job_data['job_is_remote'],
            "job_posted_at_datetime_utc":job_data['job_posted_at_datetime_utc'],
            "job_city":job_data['job_city'],
            "job_state":job_data['job_state'],
            "job_country":job_data['job_country'],
            "job_benefits":job_data['job_benefits'],
            "job_google_link":job_data['job_google_link'],
            "job_offer_expiration_datetime_utc":job_data['job_offer_expiration_datetime_utc'],
            "job_required_experience":job_data['job_required_experience'],
            "job_required_skills":job_data['job_required_skills'],
            "job_min_salary":job_data['job_min_salary'],
            "job_max_salary":job_data['job_max_salary'],
            "job_salary_currency":job_data['job_salary_currency'],
            "job_salary_period":job_data['job_salary_period'],
            "job_highlights":job_data['job_highlights'],
            "job_posting_language":job_data['job_posting_language']
}
        job_data = self.convert_json_strings(job_list)
        return Job(**job_data)

    def load_jobs(self):
        querystring = {"query": self.query, "page": "1", "pages": self.pages, "date_posted": self.posted}
        print(querystring)
        try:
            response = requests.get(self.url, headers=self.headers, params=querystring)
            response.raise_for_status()  # Check for HTTP request errors
            print(response.status_code)
            raw = response.json()
            dat = raw.get("data")
            print(len(dat))
            return dat

        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data from the API: {str(e)}")
            return None

    def save_jobs(self, dat):
        # Saving to the Job model items in the list in bulk
        jobs_to_create = []

        try:
            for job in dat:
                if job is not None:
                    if isinstance(job, dict) and "employer_name" in job:
                        job_instance = self.create_job_instance(job)
                        print(job_instance)
                        jobs_to_create.append(job_instance)
                    else:
                        print(f"Skipping invalid job: {job}")

            if jobs_to_create:
                Job.objects.bulk_create(jobs_to_create)
                logging.info("Save success")
            else:
                logging.warning("No valid jobs to save")

        except Exception as e:
            logging.error(f"Error saving jobs to the database: {str(e)}")


"""
data_fetcher = JobFetcher(query="Software Developer", pages=2)
job_data = data_fetcher.load_jobs()
# print(job_data)
data_fetcher.save_jobs(job_data)"""


"""

def save_jobs():

    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {"query":"Python developer in remote, USA","page":"1","num_pages":"1"}

    headers = {
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    print(querystring)
    response = requests.get(url, headers=headers, params=querystring)
    raw = response.json()
    dat = raw.get('data')
    # print("data: ", dat)
    # Saving to job model items in the list in bulk

    jobs_to_create = []

    for job in dat:
        if job is not None:
            # Check if 'job' is a dictionary with 'employer_name' key
            if isinstance(job, dict) and 'employer_name' in job:
                # Create a Job object and append it to the list
                jobs_to_create.append(Job(employer_name=job['employer_name'],
                    employer_logo=job['employer_logo'],
                    employer_website=job['employer_website'],
                    employer_company_type=job['employer_company_type'],
                    job_publisher=job['job_publisher'],
                    job_id=job['job_id'],
                    job_employment_type=job['job_employment_type'],
                    job_title=job['job_title'],
                    job_apply_link=job['job_apply_link'],
                    job_apply_is_direct=job['job_apply_is_direct'],
                    job_description=job['job_description'],
                    job_is_remote=job['job_is_remote'],
                    job_posted_at_timestamp=job['job_posted_at_timestamp'],
                    job_posted_at_datetime_utc=job['job_posted_at_datetime_utc'],
                    job_city=job['job_city'],
                    job_state=job['job_state'],
                    job_country=job['job_country'],
                    job_benefits=job['job_benefits'],
                    job_google_link=job['job_google_link'],
                    job_offer_expiration_datetime_utc=job['job_offer_expiration_datetime_utc'],
                    job_offer_expiration_timestamp=job['job_offer_expiration_timestamp'],
                    job_required_experience=job['job_required_experience'],
                    job_required_skills=job['job_required_skills'],
                    job_min_salary=job['job_min_salary'],
                    job_max_salary=job['job_max_salary'],
                    job_salary_currency=job['job_salary_currency'],
                    job_salary_period=job['job_salary_period'],
                    job_highlights=job['job_highlights'],
                    job_job_title=job['job_job_title'],
                    job_posting_language=job['job_posting_language']))  # Provide a value for job_salary_currency or set it as needed
                    # Use bulk_create to insert multiple records in a single query
                Job.objects.bulk_create(jobs_to_create)
                all_objects = Job.objects.all()
                return 'Save sucess'
            else:
                # Handle the case where 'job' is not in the expected format
                print(f"Skipping invalid job: {job}")
        else:
            # Handle the case where 'job' is None
            print("Encountered a None value in the list of jobs.")

fetch = save_jobs()
"""
