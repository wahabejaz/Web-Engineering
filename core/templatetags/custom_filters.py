from django import template

register = template.Library()

@register.filter
def split_string(value, separator=','):
    """Split a string by the given separator"""
    if not value:
        return []
    return value.split(separator)

@register.filter
def strip_string(value):
    """Strip whitespace from a string"""
    if not value:
        return ''
    return str(value).strip()

@register.filter
def get_item(dictionary, key):
    """Get an item from a dictionary"""
    if isinstance(dictionary, dict):
        return dictionary.get(key, '')
    return ''
