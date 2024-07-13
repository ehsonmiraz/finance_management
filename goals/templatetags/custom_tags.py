from django import template

register = template.Library()

@register.filter
def percentage(value, total):
    try:
        per= int((value / total) * 100)
        return str(per)+'%' if per<100 else '100%'
    except (ValueError, ZeroDivisionError):
        return 0

