from django import template

register = template.Library()


def multiply(value, args):
    return value*args


register.filter('multiply', multiply)