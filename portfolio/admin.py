from django.contrib import admin

# Register your models here.

from .models import Name

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('Email','First_name','Last_name','Middle_name')
    search_fields = ('Email','First_name','Last_name')
    prepopulated_fields = {'slug':('First_name','Last_name',)}
admin.site.register(Name, PortfolioAdmin)
