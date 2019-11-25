from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'evalhubapp/index.html')


def surveys(request):
    return render(request, 'evalhubapp/surveys.html')
