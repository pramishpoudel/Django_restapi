from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def students(request):
    context=[{
        'name':'pramish poudel',
        'age':21,
        'address':'kathmandu',
    }]
    return HttpResponse(context)


def about(request):
    return HttpResponse("This is about page")


