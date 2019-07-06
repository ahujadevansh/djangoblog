from urllib.parse import quote_plus
from django import template

# https://docs.djangoproject.com/en/2.2/howto/custom-template-tags/


register = template.Library()

@register.filter
def url_encoded(value):
    return quote_plus(value)