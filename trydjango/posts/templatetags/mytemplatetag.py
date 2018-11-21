from django import template

register = template.Library()


@register.filter()
def my_upper(value):  # Only one argument.
    return value.upper()
