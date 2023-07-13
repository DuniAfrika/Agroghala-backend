from django.contrib import admin
from .models import Farmer


class FarmerAdmin(admin.ModelAdmin):
    class Meta:
        model = Farmer
        fields = ('first_name', 'last_name', 'email', 'phone', 'location')

admin.site.register(Farmer, FarmerAdmin)
