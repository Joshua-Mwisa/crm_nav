from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def pinterestView(request):
    return render(request, 'social-media/pinterest.html')
