from django.contrib import admin
# pyrefly: ignore [missing-import]
from .models import Product
# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)