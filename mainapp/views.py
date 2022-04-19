from django.shortcuts import render

def index(request):
    return render(request, "mainapp/index.html")

def contact(request):
    return render(request, "mainapp/basic.html", {'values': ['if you have any quastion', 
    '330033100', 'abdumidjon@gmail.com']})