from django.contrib import admin
from .models import Cliente

# Register your models here.

class Cliente_Admin(admin.ModelAdmin):
    list_display = ['nome_cliente']


admin.site.register(Cliente, Cliente_Admin)
    