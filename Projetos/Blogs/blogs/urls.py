"""
URL configuration for blogs app.

"""
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page that shows all news.
    path('latest_news/', views.latest_news, name='latest_news'),
    # Page that show a selected new.
    path('latest_news/<int:latest_news_id>/', views.news, name='news'),
    # Page to create a new post.
    path('create_post/', views.create_post, name='create_post'),
    # Page to create a news of the post.
    path('create_news/<int:latest_news_id>/', views.create_news, name='create_news'),
    # Page to edit a news of the post.
    path('edit_news/<int:news_id>/', views.edit_news, name='edit_news'),
]