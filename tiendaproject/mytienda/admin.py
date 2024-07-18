

from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','characteristics', 'description',  'price', 'stock', 'created_at', 'category')  
    list_filter = ('created_at', 'price', 'category')  

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
