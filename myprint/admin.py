from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin
from django.utils.html import format_html

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
    list_per_page = 2
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)


class SettingsAdmin(admin.ModelAdmin):
    list_display = [
        'key',
        'value'
    ]
    list_per_page = 1
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
    list_per_page = 1
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
    list_per_page = 1
    class Meta:
        model = AboutImage
admin.site.register(AboutImage, AboutImageAdmin)





class BookInLineAdmin(admin.TabularInline):
    model = OrderForm


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInLineAdmin]
    list_per_page = 1
admin.site.register(Customer, AuthorAdmin)




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

    class Meta:
        model = OrderService
    list_per_page = 2

admin.site.register(OrderService, OrderServiceAdmin)