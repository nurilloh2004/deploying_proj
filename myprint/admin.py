from django.contrib import admin
from .models import *
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class OrderFormAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'student', 'status_order',
        'amount', 'price', 'price_free_VAT','VAT',
        'price_with_VAT', 'total', 'total_price_with_VAT', 'total_price_ALL'
    ]
    list_display_links = ['name']
admin.site.register(OrderForm , OrderFormAdmin)

@admin.register(Customer)
class CustomerAdmin(TranslationAdmin):
    list_display = [
        'id_name_order', 'client', 'client_phone_number',
        'manager_name', 'date_order', 'ready_product_date_order'
    ]
    list_display_links = ['client']


@admin.register(Type)
class TypeAdmin(TranslationAdmin):
    list_display = [
        'name',
    ]
    list_display_links = [
        'name',
    ]
    list_per_page = 3



admin.site.register(User)
admin.site.register(InfoProduct)
# admin.site.register(Product)
# admin.site.register(Tariff)
# admin.site.register(MenuTariff)
admin.site.register(Sponsors)


@admin.register(Portfolio)
class PortfolioAdmin(TranslationAdmin):
    list_display = [
        'name', 'image'
    ]
    list_display_links = [
        'name',
    ]
    list_per_page = 3
###################################################################


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


@admin.register(Design)
class DesigneAdmin(TranslationAdmin):
    list_display = [
        'name', 'slug', 'description',
        'image1', 'image2', 'image3'
    ]
    list_display_links = ['name']



###################################################################
@admin.register(TypeService)
class TypeServiceAdmin(TranslationAdmin):
    list_display = [
        'name', 'image'
    ]
    list_display_links = [
        'name'
    ]
    list_per_page = 3





@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = [
        'name'
    ]
    list_display_links = [
        'name'
    ]
    class Meta:
        model = Category




class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category', 'name', 'image',
    ]
    list_display_links = [
        'name'
    ]
    class Meta:
        model = SubCategory

admin.site.register(SubCategory, SubCategoryAdmin)




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

@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = [
        "description"
    ]
    list_display_links = [
        "description"
    ]
    list_per_page = 1
    search_fields = ('description','')


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
# @admin.register(DigitalPrint)
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



class ProductOrderAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'vendor_code', 'phone', 'creat_add'
    ]
    list_display_links = [
        'name', 'vendor_code',
    ]
    class Meta:
        model = Product_Orders

admin.site.register(Product_Orders, ProductOrderAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'category', 'subcategory', 'name', 'image', 'info_product', 'vendor_code', 'description'
    ]
    list_display_links = [
        'name', 'vendor_code',
    ]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)