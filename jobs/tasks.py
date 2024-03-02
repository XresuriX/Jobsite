from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.management import call_command
from api import JobFetcher
import json

"""Task for loading jobs"""
@shared_task
def fetch_data():
    data_fetcher = JobFetcher(query="Software Developer", pages=2, posted="today")
    job_data = data_fetcher.load_jobs()
    try:
        if job_data:
            data_fetcher.save_jobs(job_data)
            return f"Saved {len(job_data)} jobs."  
        else:
            return "No jobs fetched or saved."
    except Exception as e:
        # If saving to the database fails, save the data to a text file
        with open('failed_job_data.txt', 'w') as file:
            json.dump(job_data, file)
        return f"Failed to save jobs to the database. Saved {len(job_data)} jobs to 'failed_job_data.txt'. Error: {str(e)}" # type: ignore
        
    
@shared_task
def add(x, y):
    return x + y 