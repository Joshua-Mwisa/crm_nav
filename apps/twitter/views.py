from django.shortcuts import render
from django.views.generic import TemplateView
import tweepy
# Create your views here.


def TwitterView(request):
    
    return render(request,'social-media/twitter.html', {"trends": trends_result[0]["trends"]})


# Authenticate to Twitter
auth = tweepy.OAuthHandler("EQqK3RmbbFD0uFcR7nVebzU3p", "ISlMZ4tmKrUJBIn6YsDqRR8aSpRANa7i1J4UN38liNKgK3m7ib")
auth.set_access_token("1371532600112734215-xmhdWNOoQP1ec7LuRxWNBm2owCCHKI", "Q9ayJzTvZyN9wZVwZgxGnHxVupnou5JIE55VYpKQZDGq0")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
trends_result = api.trends_place(1)[:10]


def TwitterSearch(request):
    searchItem=request.POST.get('searchItem')
    searchResults=tweepy.Cursor(api.search, q=searchItem, lang="en").items(50)
    return render(request, 'social-media/twitter.html', {"searchResults": searchResults, "trends": trends_result[0]["trends"]})
