from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin
from django.utils.html import format_html

# Register your models here.
admin.site.register(InfoType )
admin.site.register(Type)
admin.site.register(User)
admin.site.register(InfoProduct)
# admin.site.register(Product)
admin.site.register(Tariff)
admin.site.register(MenuTariff)
admin.site.register(Sponsors)
admin.site.register(Contact)
admin.site.register(Portfolio)
admin.site.register(Form)

###################################################################
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    class Model:
        model = Type2
admin.site.register(Type2, TypeAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = [
        'type_sevice', 'image'
    ]
    list_display_links = [
        'type_sevice',
    ]
    list_per_page = 2
    class Meta:
        model = Image2


admin.site.register(Image2, ImageAdmin)

class DesigneAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'description',
        'image1', 'image2', 'image3'
    ]
    list_display_links = ['name']

    class Meta:
        model = Design

admin.site.register(Design, DesigneAdmin)


###################################################################

class TypeServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'image'
    ]
    list_display_links = [
        'name'
    ]
    list_per_page = 2
    class Meta:
        model = TypeService


admin.site.register(TypeService, TypeServiceAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'category', 'name',  'image', 'info_product',
        'vendor_code', 'description'
    ]
    list_display_links = [
        'category', 'name'
    ]
    list_per_page = 2
    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)




class CategoryAdmin(admin.ModelAdmin):
    fields = [
        'parent', 'name', 'image'
    ]
    list_display = [
        'id', 'parent', 'name','image'
    ]
    list_display_links = [
        'parent', 'name',
    ]
    list_per_page = 2
    search_fields = ('parent', 'name')
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)


class SettingsAdmin(admin.ModelAdmin):
    list_display = [
        'key',
        'value'
    ]
    list_per_page = 1
    search_fields = ('key', 'value')
    class Meta:
        model = Settings
admin.site.register(Settings, SettingsAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = [
        "description"
    ]
    list_display_links = [
        "description"
    ]
    list_per_page = 1
    search_fields = ('description','')
    class Meta:
        model = About
admin.site.register(About, AboutAdmin)

class AboutImageAdmin(admin.ModelAdmin):
    list_display = [
        "name", "image"
    ]
    list_display_links = [
        "name",
    ]
    list_per_page = 1
    search_fields = ('name','image')
    class Meta:
        model = AboutImage
admin.site.register(AboutImage, AboutImageAdmin)







##################################################
class ServiceeIneLineAdmin(admin.TabularInline):
    model = SubDigitalPrint



class AuthoreAdmin(admin.ModelAdmin):
    inlines = [ServiceeIneLineAdmin]

admin.site.register(DigitalPrint, AuthoreAdmin)


##################################################

class ServiceIneLineAdmin(admin.TabularInline):
    model = SubLargeFormat



class AuthorAdmin(admin.ModelAdmin):
    inlines = [ServiceIneLineAdmin]

admin.site.register(LargeFormat, AuthorAdmin)


##################################################

##################################################
class ServiceeIneLineAdminn(admin.TabularInline):
    model = SUbTextPrint



class AuthoreAdminn(admin.ModelAdmin):
    inlines = [ServiceeIneLineAdminn]

admin.site.register(TextPrint, AuthoreAdminn)


##################################################


##################################################
class ServiceeIneLineAdminn(admin.TabularInline):
    model = SubLaserPrint



class AuthoreAdminn(admin.ModelAdmin):
    inlines = [ServiceeIneLineAdminn]

admin.site.register(LaserPrint, AuthoreAdminn)


##################################################


class OrderServiceAdmin(admin.ModelAdmin):
    list_display = [
        'order_type', 'username', 'phone_number',
        'creat_add'
    ]
    list_display_links = [
        'order_type', 'username'
    ]
    search_fields = ('username','phone_number')
    class Meta:
        model = OrderService
    list_per_page = 2

admin.site.register(OrderService, OrderServiceAdmin)