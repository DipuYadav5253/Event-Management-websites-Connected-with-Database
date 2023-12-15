# custom_table/admin.py

from django.contrib import admin
from .models import EventOrganizer
from .models import UserRegistration


@admin.register(EventOrganizer)
class EventOrganizerAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'event_type', 'event_date')  # Customize the fields you want to display in the admin list view
    list_filter = ('event_type',)  # Add filters for specific fields
    search_fields = ('fullname', 'email', 'event_venue')  # Add search functionality for specific fields
# admin.py
 
 
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'username', 'email', 'gender', 'enrollment']
    list_filter = ['gender']
    search_fields = ['fullname', 'username', 'email']
    # Add more customization as needed

# Register the UserRegistration model with the custom admin class
admin.site.register(UserRegistration, UserRegistrationAdmin)
