from django.shortcuts import render
from django.http import HttpResponse
import discord
from discord import Webhook
import aiohttp

def home(request):
    return render(request, 'home.html')

def invited(request):
    return render(request, 'invited.html')

def terms(request):
    return render(request, 'terms.html')

def tos(request):
    return render(request, 'tos.html')

def privacy(request):
    return render(request, 'privacy.html')