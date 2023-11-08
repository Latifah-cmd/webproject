from django.contrib import admin
from .models import Client
from .models import Product
from .models import Transaction

class ClientAdmin(admin.ModelAdmin):
    list_display= ("first_name","last_name","contact","email","address","product","size","payment_opts")
    #list_filter = ("first_name","email"),
    #search_fields =("email"),

admin.site.register( Client,ClientAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=("product_id","category_id","product_name","unit_price","sale_price","available_stock","unit_measure","date_updated")
    #list_filter =("sale_price","unit_price"),
    #search_fields=("date_updated","available_stock"),
admin.site.register(Product,ProductAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_id","Product_id","transaction_type","stock_taken","transaction_amount","transaction_date")
    #list_filter=("stock_taken","transaction_date"),
    #search_fields=("transaction_date","transaction_type"),

admin.site.register(Transaction,TransactionAdmin)

