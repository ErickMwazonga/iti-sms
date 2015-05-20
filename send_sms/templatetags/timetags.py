__author__ = 'shanecrossan'
#Django
from django import template

#Lib
import datetime
register = template.Library()

def print_timestamp(timestamp):
    try:
        #assume, that timestamp is given in seconds with decimal point
        ts = float(timestamp)
        ts += 7200
    except ValueError:
        return None
    if timestamp != 0:
        return datetime.datetime.fromtimestamp(ts)
    else:
        return ''

register.filter(print_timestamp)