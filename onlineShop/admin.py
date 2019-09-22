from django.contrib import admin

# Register your models here.
from .models import MainCategory, Category, SubCategory, Product

class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(MainCategory, MainCategoryAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = { 'slug': ('name',)}

admin.site.register(SubCategory, SubCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'available', 'created_at', 'updated_at', ]
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'quantity', 'available',]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


#admin.site.register(Profile)