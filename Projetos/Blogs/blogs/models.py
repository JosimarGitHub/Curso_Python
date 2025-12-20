from django.db import models

# Create your models here.
class LatestNews(models.Model):
    """The latest news about Tecnology"""
    text = models.CharField(max_length=800)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Latest News'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class News(models.Model):
    """The selected news someone choose"""
    latest_news = models.ForeignKey(LatestNews, on_delete=models.CASCADE)

    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'
    
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text}"
