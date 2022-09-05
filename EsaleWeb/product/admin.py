from django.contrib import admin
from .models import Product,ProductDetail,Category,Color,size
# Register your models here.

class productAdmin(admin.ModelAdmin):
     list_display = ['name','codeNo','price','description','active','orginal']
    # fieldsets=(
    #     (None, {
    #         'fields': ('name','codeNo','price','description','active','orginal')
    #     }),
    #     ('ProductDetail', {
    #         'classes': ('wide',),
    #         'fields': ('detailName','value' ),
    #     }),
    # )




admin.site.register(Product,productAdmin)
admin.site.register(ProductDetail)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(size)

