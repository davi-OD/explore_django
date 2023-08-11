from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, You are currently at polls page!")
    # return JsonResponse({"title": "Helloo, you are at parts"})