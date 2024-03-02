from django.views.generic import TemplateView, ListView, DetailView
from django_filters.views import FilterView
from django.shortcuts import render, redirect
from jobs.models import Job
from jobs.filters import JobFilter


def home(request):
    return render(request, 'jobs/home.html')

def about(request):
    return render(request, 'jobs/about.html')

def dev(request):
    jobs = Job.objects.all()

    context = {'jobs': jobs}
    return render(request, 'jobs/dev.html', context)

class JobsView(ListView, FilterView):
    model = Job
    template_name = 'jobs/details.html'
    context_object_name = 'jobs'
    filterset_class = JobFilter
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

class JobDetailView(DetailView):
    """Detail view that also acts as a list view for searching"""
    model = Job
    template_name = 'jobs/details.html'  

    paginate_by = 5  

    def get_queryset(self):
       
        return Job.objects.all()

    def get_context_data(self, **kwargs):
        """function that list data to be displayed and displays job details when the user selects one"""
        context = super().get_context_data(**kwargs)
        
        job_filter = JobFilter(self.request.GET, queryset=Job.objects.all())
        filtered_jobs = job_filter.qs

        context['jobs'] = filtered_jobs
        context['job_filter'] = job_filter
        return context