from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin

# Register your models here.
admin.site.register(InfoType )
admin.site.register(Type)
admin.site.register(User)
# admin.site.register(InfoProduct)
# admin.site.register(Product)
admin.site.register(Tariff)
admin.site.register(MenuTariff)
admin.site.register(Sponsors)
admin.site.register(Contact)
admin.site.register(Portfolio)
admin.site.register(Form)
# admin.site.register(OrderForm)x
# admin.site.register(Customer)





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

# admin.site.register(Category, CategoryAdmin)


class SettingsAdmin(admin.ModelAdmin):
    list_display = [
        'key',
        'value'
    ]

    class Meta:
        model = Settings
admin.site.register(Settings, SettingsAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = [
        "description_uz"
    ]
    list_display_links = [
        "description_uz"
    ]
    class Meta:
        model = About
admin.site.register(About, AboutAdmin)

class AboutImageAdmin(admin.ModelAdmin):
    list_display = [
        "name_uz", "image"
    ]
    list_display_links = [
        "name_uz",
    ]
    class Meta:
        model = AboutImage
admin.site.register(AboutImage, AboutImageAdmin)





class BookInLineAdmin(admin.TabularInline):
    model = OrderForm


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInLineAdmin]

admin.site.register(Customer, AuthorAdmin)




class BookIneLineAdmin(admin.TabularInline):
    model = Product



class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookIneLineAdmin]

admin.site.register(Category, AuthorAdmin)





class ServiceIneLineAdmin(admin.TabularInline):
    model = MenuService



class AuthorAdmin(admin.ModelAdmin):
    inlines = [ServiceIneLineAdmin]

admin.site.register(TypeService, AuthorAdmin)