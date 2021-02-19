from django import template
from ..urls import r
from django.utils.html import mark_safe

register = template.Library()

@register.simple_tag
def vue_routes():
    vroutes = r.get_vroute()
    return mark_safe(vroutes)
