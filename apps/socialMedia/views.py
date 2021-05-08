from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

import json


@login_required
def linkedinView(request):
    return render(request, 'social-media/linkedin.html')


@login_required
def facebookView(request):
    return render(request, 'social-media/facebook.html')


@login_required
def twitterView(request):
    return render(request, 'social-media/twitter.html')


@login_required
def whatsappView(request):
    return render(request, 'social-media/whatsapp.html')


@login_required
def telegramView(request):
    return render(request, 'social-media/telegram.html')


@login_required
def youtubeView(request):
    return render(request, 'social-media/youtube.html')


@login_required
def tiktokView(request):
    return render(request, 'social-media/tiktok.html')


@login_required
def snapchatView(request):
    return render(request, 'social-media/snapchat.html')


@login_required
def quoraView(request):
    return render(request, 'social-media/quora.html')


@login_required
def redditView(request):
    return render(request, 'social-media/reddit.html')


@login_required
def pinterestView(request):
    return render(request, 'social-media/pinterest.html')
