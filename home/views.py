from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    db = [
        {'name':"Mohan", 'age':32},
        {'name':"Akshat", 'age':15},
        {'name':"Abhay", 'age':28},
        {'name':"Rohit", 'age':27},
        {'name':"Shubham", 'age':17},
    ]
    text = 'Hi I am coming from a DataBase File'
    return render(request, "index.html", context= { 'db': db, 'text': text})

def success(request):
    return HttpResponse("<h1>This is a success Page</h1>")

def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contacts.html")