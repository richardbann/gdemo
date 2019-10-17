from django.contrib import admin

import markdown
from markdown import extensions
from markdown.extensions import codehilite, fenced_code

from blog import models


class EscapeHtml(extensions.Extension):
    def extendMarkdown(self, md):
        md.preprocessors.deregister('html_block')
        md.inlinePatterns.deregister('html')


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ("owner", "html",)
    save_on_top = True

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.html = markdown.markdown(
            obj.source, output_format="html5",
            extensions=[
                EscapeHtml(),
                codehilite.CodeHiliteExtension(),
                fenced_code.FencedCodeExtension(),
            ]
        )
        super().save_model(request, obj, form, change)
