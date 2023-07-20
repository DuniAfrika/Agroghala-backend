from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class GhalaAdmin(admin.ModelAdmin):
    class Meta:
        model = Ghala
        fields = '__all__'

admin.site.register(Ghala, GhalaAdmin)

class SokoAdmin(admin.ModelAdmin):
    class Meta:
        model = Soko
        fields = '__all__'

admin.site.register(Soko, SokoAdmin)