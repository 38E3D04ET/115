from django import template

register = template.Library()


BAD_WORDS = ["сосиска", "редиска", "нехороший человек"]


@register.filter()
def censor(value):

   for word in BAD_WORDS:
       value = value.replace(word[1:], '*' * (len(word)-1))

   return value