from django.urls import path
from . views import linkedinView, facebookView, twitterView, instagramView, \
    whatsappView, telegramView, youtubeView, tiktokView, snapchatView, \
    quoraView, redditView, pinterestView

app_name = 'socialMedia'

urlpatterns = [
    path('linkedin', linkedinView, name='linkedin'),
    path('facebook', facebookView, name='facebook'),
    path('twitter', twitterView, name='twitter'),

    path('instagram', instagramView, name='instagram'),
    path('whatsapp', whatsappView, name='whatsapp'),
    path('telegram', telegramView, name='telegram'),

    path('youtube', youtubeView, name='youtube'),
    path('tiktok', tiktokView, name='tiktok'),
    path('snapchat', snapchatView, name='snapchat'),

    path('quora', quoraView, name='quora'),
    path('reddit', redditView, name='reddit'),
    path('pinterest', pinterestView, name='pinterest'),
]
