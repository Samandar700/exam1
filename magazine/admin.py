from django.contrib import admin

from magazine.models import (
    Category, Product, ProductImage,
    Tags, Color, Size, Brand, Banner,
    Blog, Contact, Users, ShoppingCart
)

admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Tags)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(Banner)
# admin.site.register(Contact)
admin.site.register(Users)

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'status')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ('email', )


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'rating')
    search_fields = ('name', 'rating')
    inlines = [ProductImageInline, ]







