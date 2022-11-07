from modeltranslation.translator import TranslationOptions, register
from .models import *
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
@register(Product)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
#####################################################
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
#####################################################
@register(Type)
class TypeTranslationOptions(TranslationOptions):
    fields = ('name',)
#####################################################
@register(TypeService)
class TypeServiceTranslationOptions(TranslationOptions):
    fields = ('name',)
#####################################################
@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('name',)
#####################################################
@register(Customer)
class CustomerTranslationOptions(TranslationOptions):
    fields = ('id_name_order',)
#####################################################

#####################################################
@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('description',)
#####################################################
@register(Design)
class DesignTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
#####################################################
