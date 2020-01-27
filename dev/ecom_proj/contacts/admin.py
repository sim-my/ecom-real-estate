from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'name', 'email', 'contact_date')
    list_display_links = ('id', 'listing', 'name')
    search_fields = ('name', 'listing', 'email')
    list_filter = ('listing',)
    list_per_page = 20

admin.site.register(Contact, ContactAdmin)