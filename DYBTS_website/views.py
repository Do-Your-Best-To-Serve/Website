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

def vote(request):
    if request.method == "POST":
        if request.headers.authorization == "DYBTSVOTE":
            type = request.body.type
            if type == "test":
                return HttpResponse(code=200)
            else:
                user = f"{request.body.user.name}#{request.body.user.discriminator}"
                avatar = request.body.user.avatar
                webhook_uri = "https://discord.com/api/webhooks/1023184442702958612/tFdcJB9sp7lI_XIgH8b8LQUxH3GSJEM8lMZijf_CHCjQ4_dwEyEzX1PqnVFxecLSskUF"
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(webhook_uri, session=session)
                    await webhook.edit(name=f"感謝 {user} 的投票", avatar=avatar)
                    embed = discord.Embed(title="感謝投票", description="[點我前往投票](https://discordservers.tw/bots/1008634918869418024)")
                    await webhook.send(embed=embed)
                return HttpResponse(code=200)
        else:
            return HttpResponse(code=500)
    else:
        return HttpResponse(code=500)
