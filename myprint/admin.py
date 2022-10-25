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


class DigitalPrintAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'description', 'size',
        'type', 'on_site_print', 'double_site_print', 'image'
    ]
    list_display_links = ['name']

    class Meta:
        model = DigitalPrint

admin.site.register(DigitalPrint, DigitalPrintAdmin)


class LargeFormatAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'description', 'product_name',
        'type', 'price', 'image1', 'image2', 'image3'
    ]
    list_display_links = ['name']

    class Meta:
        model = LargeFormat

admin.site.register(LargeFormat, LargeFormatAdmin)

class TextPrintAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'size', 'price',
        'description', 'image'
    ]
    list_display_links = ['name']

    class Meta:
        model = TextPrint

admin.site.register(TextPrint, TextPrintAdmin)

class LaserPrintAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'size', 'price',
        'description', 'image'
    ]
    list_display_links = ['name']

    class Meta:
        model = LaserPrint

admin.site.register(LaserPrint, LaserPrintAdmin)
###################################################################
# admin.site.register(HomeDescription)/

# admin.site.register(AboutImage)
# admin.site.register(OrderForm)x
# admin.site.register(Customer)
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





# class BookInLineAdmin(admin.TabularInline):
#     model = LargeFormat

# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [BookInLineAdmin]
#     list_per_page = 1
# admin.site.register(TableLarge, AuthorAdmin)
# class BookInLineAdmin(admin.TabularInline):
#     model = Book


# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [BookInLineAdmin]

# admin.site.register(Author, AuthorAdmin)



# class BookIneLineAdmin(admin.TabularInline):
#     model = Product



# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [BookIneLineAdmin]

# admin.site.register(Category, AuthorAdmin)

# admin.site.register(OrderService)



# class ServiceIneLineAdmin(admin.TabularInline):
#     model = MenuService



# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [ServiceIneLineAdmin]

# admin.site.register(TypeService, AuthorAdmin)


class TypeAdminService(admin.ModelAdmin):
    readonly_fields = ('photo_tag1', 'photo_tag2', 'photo_tag3')
    list_display = [
        'id', 'size', 'type_paper', 'one_site_print',
        'double_site_print', 'shiroki_size', 'shiroki_name', 'shiroki_price',
        'tekstil_size', 'tekstil_price', 'lazer_size', 'lazer_price',
        'photo_tag1', 'photo_tag2', 'photo_tag3'
    ]
    list_display_links = [
        'size', 'type_paper', 'one_site_print',
        'double_site_print'
    ]
    list_filter = ('type', )
    list_per_page = 1
    search_fields = ('type_paper','size')
    def photo_tag1(self, obj):
        return format_html(f'<img src="{obj.image1.url}" style="height:100px; width:100px; border-radius: 50%">')
    def photo_tag2(self, obj):
        return format_html(f'<img src="{obj.image2.url}" style="height:100px; width:100px; border-radius: 50%">')
    def photo_tag3(self, obj):
        return format_html(f'<img src="{obj.image3.url}" style="height:100px; width:100px; border-radius: 50%">')
    class Meta:
        model = Type_Services
admin.site.register(Type_Services, TypeAdminService)


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