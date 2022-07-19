from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,'DReports/index.html')

def add_report(request):
    return render(request,'DReports/add_report.html')
