from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def youtubeView(request):
    return render(request, 'social-media/youtube.html')
