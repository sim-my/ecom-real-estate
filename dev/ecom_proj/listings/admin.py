from django.contrib import admin

from . models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'address', 'price', 'list_date', 'is_published', 'realtor')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('city', 'realtor')
    search_fields = ('city', 'address', 'realtor__name', 'description', 'title', 'price')
    list_per_page = 20

admin.site.register(Listing, ListingAdmin)

# Register your models here.
