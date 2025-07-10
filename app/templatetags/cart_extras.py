# app/templatetags/cart_extras.py

from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    try:
        return dictionary.get(str(key), 0)
    except:
        return 0

@register.filter(name='multiply')
def multiply(value, arg):
    try:
        return int(value) * int(arg)
    except:
        return 0
