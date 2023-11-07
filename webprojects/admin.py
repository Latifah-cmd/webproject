from django.contrib import admin
from .models import Client
from .models import Product
from .models import Transaction

class ClientAdmin(admin.ModelAdmin):
    list_display= ("first_name","last_name","contact","email","address","product","size","payment_opts")

admin.site.register( Client,ClientAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=("product_id","category_id","product_name","unit_price","sale_price","available_stock","unit_measure","date_updated")

admin.site.register(Product,ProductAdmin)



