#!/usr/bin/env python

import markdown
from markdown.extensions import codehilite, fenced_code


if __name__ == '__main__':
    markdown.markdownFromFile(
        input="test.md",
        output="test.html",
        extensions=[
            codehilite.CodeHiliteExtension(),
            fenced_code.FencedCodeExtension()
        ]
    )
