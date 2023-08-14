from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Hello, You are currently at parts page!")
    return render(request, "home1.htm")