from django import template

import html

register = template.Library()

@register.filter
def show_only_first_p(value):
    post = value
    first_paragraph = ""
    if "</p>" in post:
        i_end = post.index("</p>") + 4
        first_paragraph = post[0: i_end]
    else:
        i_end = post.index("\n") -1
        first_paragraph = post[0: i_end]
    return first_paragraph