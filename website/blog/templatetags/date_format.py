from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()  #自定义filter时必须加上


@register.filter(is_safe=True)
@stringfilter  #希望字符串作为参数
def date2Year(value):
    sp = value.split('-')
    return sp[0]

@register.filter(is_safe=True)
@stringfilter  # 希望字符串作为参数
def date2Month(value):
    sp = value.split('-')
    return '%s-%s' % (sp[1], sp[2])
