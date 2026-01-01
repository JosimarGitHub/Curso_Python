from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.exceptions import PermissionDenied
import bleach
from .models import LatestNews, News
from .forms import LatestNewsForm, NewsForm

# Create your views here.

def index(request):
    """Information in Home Page"""
    return render(request, 'blogs/index.html')

def latest_news(request):
    """Information in Latest News page"""
    latest_news = LatestNews.objects.order_by('date_added')
    context = {'latest_news': latest_news}
    return render(request, 'blogs/latest_news.html', context)

def news(request, latest_news_id):
    """Show a sigle news."""
    latest_news = LatestNews.objects.get(id=latest_news_id)
    news = latest_news.news_set.order_by('-date_added')
    context = {'latest_news': latest_news, 'news': news}
    return render(request, 'blogs/news.html', context)
@login_required
def create_post(request):
    """Add a new post"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = LatestNewsForm()
    else:
        # POST data submitted; process data
        form = LatestNewsForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:latest_news')
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/create_post.html', context)
@login_required
def create_news(request, latest_news_id):
    """Add a new entry for a particular topic"""
    latest_news = LatestNews.objects.get(id=latest_news_id)

    if request.method != 'POST':
        check_post_owner(latest_news.owner, request.user)
        # No data submitted; create a blank form
        form = NewsForm()
    else:
        check_post_owner(latest_news.owner, request.user)
        # POST data submitted; process data
        form = NewsForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.latest_news = latest_news

            # --- INÍCIO DA SANITIZAÇÃO ---

            # 1. Definimos quais tags e atributos são permitidos (Lista Branca)
            allowed_tags = ['p', 'b', 'i', 'u', 'em', 'strong', 'a', 'br', 'ul', 'ol', 'li']
            allowed_attrs = {
                'a': ['href', 'title', 'target'], # Permite o link do seu vídeo
            }

            # 2. Limpamos o campo 'text' antes de salvar
            # O bleach remove scripts e tags perigosas automaticamente
            cleaned_text = bleach.clean(
                new_post.text, 
                tags=allowed_tags, 
                attributes=allowed_attrs,
                strip=True # Remove completamente tags não permitidas
            )
            
            new_post.text = cleaned_text

            # --- FIM DA SANITIZAÇÃO ---

            new_post.save()
            return redirect('blogs:news', latest_news_id=latest_news_id)
    
    # Display a blank or invalid form
    context = {'latest_news': latest_news, 'form': form}
    return render(request, 'blogs/create_news.html', context)
@login_required
def edit_news(request, news_id):
    """Edit a news for a particular topic"""
    news = News.objects.get(id=news_id)
    latest_news = news.latest_news

    if request.method != 'POST':
        check_post_owner(latest_news.owner, request.user)
        # No data submitted; create a blank form
        form = NewsForm(instance=news)
    else:
        check_post_owner(latest_news.owner, request.user)
        # POST data submitted; process data
        form = NewsForm(instance=news, data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.latest_news = latest_news

            # --- INÍCIO DA SANITIZAÇÃO ---

            # 1. Definimos quais tags e atributos são permitidos (Lista Branca)
            allowed_tags = ['p', 'b', 'i', 'u', 'em', 'strong', 'a', 'br', 'ul', 'ol', 'li']
            allowed_attrs = {
                'a': ['href', 'title', 'target'], # Permite o link do seu vídeo
            }

            # 2. Limpamos o campo 'text' antes de salvar
            # O bleach remove scripts e tags perigosas automaticamente
            cleaned_text = bleach.clean(
                new_post.text, 
                tags=allowed_tags, 
                attributes=allowed_attrs,
                strip=True # Remove completamente tags não permitidas
            )
            
            new_post.text = cleaned_text
            
            # --- FIM DA SANITIZAÇÃO ---

            new_post.save()
            return redirect('blogs:news', latest_news_id=news_id)
    
    # Display a blank or invalid form
    context = {'latest_news': latest_news, 'news': news, 'form': form}
    return render(request, 'blogs/edit_news.html', context)

def check_post_owner(owner, user):
    if owner != user:
        raise PermissionDenied