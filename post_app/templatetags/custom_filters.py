from django import template


register = template.Library()


def range_filter(value):
    if len(value)<300:
        return value
    return value[0:300]+'   - - - - - - - - - - - -- - - - -'


register.filter('range_filter', range_filter)
