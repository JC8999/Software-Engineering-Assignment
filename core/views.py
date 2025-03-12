from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def practice_areas(request):
    return render(request, 'core/practice_areas.html')
