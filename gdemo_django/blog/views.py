from django.views.generic import DetailView

from . import models


class BlogView(DetailView):
    template_name = "blog/article.html"
    model = models.Article
