from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display= ("first_name","last_name","contact","email","address","product","size","payment_opts")

admin.site.register( Client,ClientAdmin)



