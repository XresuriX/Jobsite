import django_filters
from django_filters import CharFilter
from django import forms
from .models import *


# filter for job page
class JobFilter(django_filters.FilterSet):
    job_title= CharFilter(field_name='job_title', lookup_expr="icontains", label='Job Title')
    #job_publisher = django_filters.ModelMultipleChoiceFilter(queryset=Job.objects.all(), widget=forms.CheckboxSelectMultiple(), field_name='job_publisher', lookup_expr="icontains", label='Publisher', )
    #tags = django_filters.ModelMultipleChoiceFilter(queryset=Job.objects.all(), widget=forms.CheckboxSelectMultiple())
    job_is_remote = django_filters.BooleanFilter()
    job_city = CharFilter(field_name='job_publisher', lookup_expr="icontains", label='City')
    job_state= CharFilter(field_name='job_publisher', lookup_expr="icontains", label='State ')
    job_country= CharFilter(field_name='job_publisher', lookup_expr="icontains", label='Country ')
    #job_posted_at_datetime_utc= 
    class Meta:
        model = Job
        fields = ['job_title', 'job_publisher', 'job_is_remote', 'job_city', 'job_state','job_country']
