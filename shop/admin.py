from django.contrib import admin
from .models import Product, Cart, CartProduct, Transaction
# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Transaction)
admin.site.site_header = "BootShop"