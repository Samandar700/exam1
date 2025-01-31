from django.contrib import admin
from apps.models import Category, Product, ProductImage, Tag,  Color,  Size,  Brand , Banner, Blog, Saqlovchi, Users

admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Tag)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(Banner)
admin.site.register(Users)
# admin.site.register(Blog)
# admin.site.register(Saqlovchi)

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'status')




@admin.register(Saqlovchi)
class SaqlovchiAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email' ]
    search_fields = ('email', )




class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1




@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'rating')
    search_fields = ('name', 'rating')
    inlines = [ProductImageInline,]