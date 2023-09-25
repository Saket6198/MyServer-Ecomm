from django.contrib import admin

from .models import *

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'stock')

# admin.site.register(Product, ProductAdmin)

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
