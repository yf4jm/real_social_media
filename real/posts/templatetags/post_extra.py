from django import template

register = template.Library()

@register.filter
def add_one(value):
    return value + 1

def __nonzero__(value):
    return bool(value)