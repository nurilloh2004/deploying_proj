from django.template.defaultfilters import register



@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)