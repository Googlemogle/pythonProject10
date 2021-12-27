from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(requst):
    return render(requst, 'main/index.html')


def we(request):
    return render(request,'main/we.html')