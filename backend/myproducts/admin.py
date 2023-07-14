from django.contrib import admin
from .models import *


class MyghalaAdmin(admin.ModelAdmin):
    class Meta:
        model = Myghala
        fields = '__all__'

class MysokoAdmin(admin.ModelAdmin):
    class Meta:
        model = Mysoko
        fields = '__all__'

admin.site.register(Mysoko, MysokoAdmin)
admin.site.register(Myghala, MyghalaAdmin)
