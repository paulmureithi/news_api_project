from newsapi import NewsApiClient
from decouple import config
from django.shortcuts import render


# Create your views here.
def homepage(requests):
    newsapi = NewsApiClient(api_key=config('API_KEY'))
    trending = newsapi.get_top_headlines(country='gb', category='sports')
    latest = trending['articles']
    headline = []
    description = []
    url = []
    author = []
    date = []

    for i in range(len(latest)):
        news = latest[i]
        headline.append(news['title'])
        description.append(news['description'])
        url.append(news['url'])
        author.append(news['author'])
        date.append(news['publishedAt'])

    zipped_news = zip(headline, description, url, author, date)

    context = {
        'zipped_news': zipped_news
    }

    return render(requests, 'home.html', context=context)
