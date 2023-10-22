from django.contrib import admin
from .models import Person  # Import your model

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')  # Customize the list display

admin.site.register(Person, PersonAdmin)  # Register the model with the custom admin class