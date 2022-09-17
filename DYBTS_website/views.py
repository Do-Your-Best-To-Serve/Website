from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def invited(request):
    return render(request, 'invited.html')