from django.shortcuts import render
from .models import jobs
# Create your views here.
def home(request):
    jobss = jobs.objects
    return render(request, 'jobs/home.html', {'jobss':jobss})