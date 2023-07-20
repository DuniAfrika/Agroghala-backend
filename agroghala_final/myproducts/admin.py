from django.contrib import admin
from .models import *

class MyGhalaAdmin(admin.ModelAdmin):
    class Meta:
        model = MyGhala
        fields = '__all__'

class MySokoAdmin(admin.ModelAdmin):
    class Meta:
        model = MySoko
        fields = '__all__'

admin.site.register(MyGhala, MyGhalaAdmin)
admin.site.register(MySoko, MySokoAdmin)
