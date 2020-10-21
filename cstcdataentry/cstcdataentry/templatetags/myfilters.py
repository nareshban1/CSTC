import datetime
from django import template

register = template.Library()

@register.filter
def days_until(exdate):
    delta = exdate - datetime.date.today()

    return delta.days