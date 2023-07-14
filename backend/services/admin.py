from django.contrib import admin
from .models import *

class GhalaAdmin(admin.ModelAdmin):
    class Meta:
        model = Ghala
        fields = (
            'title', 'short_description', 'full_description',
            'contact', 'email', 'location', 'start_price', 'rent_price',
            'on_demand', 'space_available', 'image'
        )

admin.site.register(Ghala, GhalaAdmin)

class SokoAdmin(admin.ModelAdmin):
    class Meta:
        model = Soko
        fields = (
            'commodity', 'last_price',
            'current_price', 'on_demand', 'image'
        )

admin.site.register(Soko, SokoAdmin)