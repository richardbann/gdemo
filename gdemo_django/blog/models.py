from django.db import models


class Article(models.Model):
    source = models.TextField(blank=True)
