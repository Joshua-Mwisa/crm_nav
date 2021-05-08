from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


@login_required
def instagramView(request):
    return render(request, 'social-media/instagram.html')
