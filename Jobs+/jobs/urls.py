from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home,
    about,
    dev,
    JobsView,
    JobDetailView

)
from . import views

app_name = 'jobs'
urlpatterns = [
   path('home', views.home, name='home'),
   path('about', views.about, name='about'),
   path('', views.dev, name='dev'),
   path('jobs', JobsView.as_view(), name='list'),
   path('jobs/<int:pk>/', JobDetailView.as_view(), name='details'),
    # path('login/', auth_views.LoginView.as_view(template_name='report/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='report/logout.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

