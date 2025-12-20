from django.shortcuts import render, redirect
from .models import LatestNews, News
from .forms import LatestNewsForm, NewsForm

# Create your views here.

def index(request):
    """Information in Home Page"""
    return render(request, 'blogs/index.xhtml')

def latest_news(request):
    """Information in Latest News page"""
    latest_news = LatestNews.objects.order_by('date_added')
    context = {'latest_news': latest_news}
    return render(request, 'blogs/latest_news.xhtml', context)

def news(request, latest_news_id):
    """Show a sigle news."""
    latest_news = LatestNews.objects.get(id=latest_news_id)
    news = latest_news.news_set.order_by('-date_added')
    context = {'latest_news': latest_news, 'news': news}
    return render(request, 'blogs/news.xhtml', context)

def create_post(request):
    """Add a new post"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = LatestNewsForm()
    else:
        # POST data submitted; process data
        form = LatestNewsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:latest_news')
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/create_post.xhtml', context)

def create_news(request, latest_news_id):
    """Add a new entry for a particular topic"""
    latest_news = LatestNews.objects.get(id=latest_news_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = NewsForm()
    else:
        # POST data submitted; process data
        form = NewsForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.latest_news = latest_news
            new_post.save()
            return redirect('blogs:news', latest_news_id=latest_news_id)
    
    # Display a blank or invalid form
    context = {'latest_news': latest_news, 'form': form}
    return render(request, 'blogs/create_news.xhtml', context)

def edit_news(request, news_id):
    """Edit a news for a particular topic"""
    news = News.objects.get(id=news_id)
    latest_news = news.latest_news

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = NewsForm(instance=news)
    else:
        # POST data submitted; process data
        form = NewsForm(instance=news, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:news', latest_news_id=latest_news.id)
    
    # Display a blank or invalid form
    context = {'latest_news': latest_news, 'news': news, 'form': form}
    return render(request, 'blogs/edit_news.xhtml', context)
