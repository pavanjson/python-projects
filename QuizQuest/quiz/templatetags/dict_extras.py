# quiz/templatetags/dict_extras.py
from django import template

register = template.Library()

@register.filter
def get(dictionary, key):
    return dictionary.get(key)
