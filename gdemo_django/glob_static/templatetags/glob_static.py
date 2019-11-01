import os

from django import template
from django.templatetags.static import StaticNode
from django.contrib.staticfiles import finders


register = template.Library()


class GlobStaticNode(StaticNode):
    @classmethod
    def handle_simple(cls, path):
        realname = os.path.basename(finders.find(path))
        dir, name = os.path.split(path)
        path = os.path.join(dir, realname)
        return StaticNode.handle_simple(path)


@register.tag
def glob_static(parser, token):
    return GlobStaticNode.handle_token(parser, token)
