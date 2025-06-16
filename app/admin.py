from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('org_id', 'name', 'link')  # Display the link in the list view
    readonly_fields = ('link',)  # Make the link field read-only in the admin