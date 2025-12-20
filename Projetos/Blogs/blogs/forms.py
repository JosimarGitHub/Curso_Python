from django import forms

from .models import LatestNews, News

class LatestNewsForm(forms.ModelForm):
    class Meta:
        model = LatestNews
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'rows': 1, 'cols': 200})}

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'rows': 50, 'cols': 250})}
