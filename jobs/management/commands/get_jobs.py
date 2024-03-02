from django.core.management.base import BaseCommand
from api import JobFetcher

"""Custom django command for loading jobs into the db"""
class Command(BaseCommand):
    help = "Fetch and import data from an external API"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        


    def handle(self, *args, **kwargs):
        try:
            self.data_fetcher = JobFetcher(query='Software Developer', pages=3, posted='today')
            self.job_data = self.data_fetcher.load_jobs()
            if self.job_data:
                self.data_fetcher.save_jobs(self.job_data)
                self.stdout.write(self.style.SUCCESS('Job data fetched and saved successfully.'))
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("Received Ctrl+C. Cleaning up..."))

            self.stdout.write(self.style.SUCCESS("Cleanup complete. Exiting..."))
