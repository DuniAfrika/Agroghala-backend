from django.contrib import admin
from .models import *

class FeedbackAdmin(admin.ModelAdmin):
    class Meta:
        model = FeedBack
        fields = '__all__'


admin.site.register(FeedBack, FeedbackAdmin)
