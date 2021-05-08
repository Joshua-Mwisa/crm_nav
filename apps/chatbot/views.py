from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy


class ChatbotView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/chatbot.html'
    login_url = reverse_lazy('login')
