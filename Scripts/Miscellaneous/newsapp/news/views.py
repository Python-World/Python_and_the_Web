import json

import requests
from django.shortcuts import render

# Create your views here.


def home(request):
    news_api_requests = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&apiKey=82b29d682aea4a05b79b1f53dc4c2f95"
    )
    api = json.loads(news_api_requests.content)
    return render(request, "home.html", {"api": api})


def bussiness(request):
    news_api_requests = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=82b29d682aea4a05b79b1f53dc4c2f95"
    )
    api = json.loads(news_api_requests.content)
    return render(request, "bussiness.html", {"api": api})


def entertainment(request):
    news_api_requests = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=82b29d682aea4a05b79b1f53dc4c2f95"
    )
    api = json.loads(news_api_requests.content)
    return render(request, "entertainment.html", {"api": api})


def sports(request):
    news_api_requests = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=82b29d682aea4a05b79b1f53dc4c2f95"
    )
    api = json.loads(news_api_requests.content)
    return render(request, "sports.html", {"api": api})
