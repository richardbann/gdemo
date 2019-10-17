from django.db import models
from django.contrib.auth import get_user_model


class Article(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    source = models.TextField(blank=True)
    html = models.TextField(blank=True)
