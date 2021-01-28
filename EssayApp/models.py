from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Essay(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse('essay-detail', kwargs={'pk': self.pk})