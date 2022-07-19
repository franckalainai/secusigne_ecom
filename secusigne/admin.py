from django.contrib import admin
from . models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('title',)

class SizeAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'color', 'size', 'category', 'status')
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('title',), }

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'color', 'size')

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)