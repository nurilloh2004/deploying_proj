from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin

# Register your models here.
admin.site.register(InfoType , TranslatableAdmin)
admin.site.register(Type, TranslatableAdmin)
admin.site.register(User, TranslatableAdmin)
admin.site.register(Banner, TranslatableAdmin)
admin.site.register(InfoProduct, TranslatableAdmin)
admin.site.register(Product, TranslatableAdmin)
admin.site.register(Printer, TranslatableAdmin)
admin.site.register(Tariff, TranslatableAdmin)
admin.site.register(MenuTariff, TranslatableAdmin)
admin.site.register(CEO, TranslatableAdmin)
admin.site.register(Sponsors, TranslatableAdmin)
admin.site.register(Contact, TranslatableAdmin)
admin.site.register(Portfolio, TranslatableAdmin)
admin.site.register(SocialMedia, TranslatableAdmin)
admin.site.register(Form, TranslatableAdmin)
admin.site.register(OrderForm, TranslatableAdmin)
admin.site.register(Customer, TranslatableAdmin)


class TypeServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name_uz', 'image'
    ]
    list_display_links = [
        'name_uz'
    ]
    class Meta:
        model = TypeService
admin.site.register(TypeService, TypeServiceAdmin, TranslatableAdmin)


class MenuServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name_uz', 'image',
        'type_service'
    ]
    list_display_links = [
        'name_uz',
    ]
    class Meta:
        model = MenuService
admin.site.register(MenuService, MenuServiceAdmin, TranslatableAdmin)

class CategoryAdmin(admin.ModelAdmin):
    fields = [
        'parent', 'name_uz', 'image'
    ]
    list_display = [
        'id', 'parent', 'name_uz','image'
    ]
    list_display_links = [
        'parent', 'name_uz',
    ]
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin, TranslatableAdmin)


class SettingsAdmin(admin.ModelAdmin):
    list_display = [
        'key',
        'value'
    ]

    class Meta:
        model = Settings
admin.site.register(Settings, SettingsAdmin, TranslatableAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = [
        "description_uz"
    ]
    list_display_links = [
        "description_uz"
    ]
    class Meta:
        model = About
admin.site.register(About, AboutAdmin, TranslatableAdmin)

class AboutImageAdmin(admin.ModelAdmin):
    list_display = [
        "name_uz", "image"
    ]
    list_display_links = [
        "name_uz",
    ]
    class Meta:
        model = AboutImage
admin.site.register(AboutImage, AboutImageAdmin, TranslatableAdmin)