from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'priority', 'price', 'created_at', 'updated_at')
    list_filter = ('category', 'status', 'priority')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    fieldsets = (
        ('General Information', {
            'fields': ('title', 'description', 'price')
        }),
        ('Classification & Workflow', {
            'fields': ('category', 'status', 'priority')
        }),
    )

# Customize Admin Site Branding
admin.site.site_header = "GigFlow Django Administration"
admin.site.site_title = "GigFlow Admin Portal"
admin.site.index_title = "Welcome to GigFlow Project & Task Management Portal"
