from django.contrib import admin
from .models import LatestNews, News

# Register your models here.

admin.site.register(LatestNews)
admin.site.register(News)