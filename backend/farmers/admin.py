from django.contrib import admin
from .models import *


class FarmerAdmin(admin.ModelAdmin):
    class Meta:
        model = Farmer
        fields = '__all__'

admin.site.register(Farmer, FarmerAdmin)
