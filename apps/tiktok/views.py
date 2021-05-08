from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def tiktokView(request):
    return render(request, 'social-media/tiktok.html')
