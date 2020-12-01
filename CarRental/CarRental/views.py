from django.shortcuts import render

def homepage(request):
    return render(request, "CarRental/home.html")

def about(request):
    return render(request, "CarRental/about.html")
