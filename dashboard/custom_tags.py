# templatetags/custom_tags.py
from django import template

register = template.Library()

@register.filter
def currency(value):
    # Assuming value is in dollars
    return "{:.0f} DA".format(value)
