from django import template
from datetime import timedelta, datetime

register = template.Library()


@register.filter(name='icon_split')
def icon_split(stri):
    sep = stri.split('</i>')[0]
    sep = sep + '</i>'
    return sep


@register.filter(name='date_return')
def date_return(i):
    date = datetime.now()
    # print('date', date)
    poj = date + timedelta(days=int(i))
    # print('poj', date)
    return poj
