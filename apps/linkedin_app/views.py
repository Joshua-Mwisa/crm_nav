from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.shortcuts import render


@login_required
def LinkedinView(request):
    return render(request, 'social-media/linkedin.html')

