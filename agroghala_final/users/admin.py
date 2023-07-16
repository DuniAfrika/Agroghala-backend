from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
#from django.forms import TextInput, Textarea
#Use above for blogs and ghala descriptions

class UserAdminConfig(UserAdmin):

        search_fields = ('email', 'first_name', 'last_name')
        list_filter=('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
        ordering = ('-date_joined',)
        list_display = (
                'first_name',
                'last_name',
                'email',
                'is_active',
                'is_staff'
        )

        fieldsets = (
            ( None, {
                    'fields': (
                            'first_name', 'last_name', 'email',
                            'password', 'address'
                    )}),
            ( 'Permissions', {
                    'fields': (
                            'is_staff', 'is_active', 'is_superuser', 'is_farmer'
                    )}),
            ('Personal', {
                    'fields': (
                            'phone_number',
                    )
            }))
        """""
        formfield_overrides = {
            #NewUser - Name of model
            #about - content overriden
            NewUser.about: { 'widget': Textarea{attrs={'rows': 10, 'cols': 40}}}
        }
        """""
        add_fieldsets = (
                ( None, {
                        'classes': ('wide',),
                        'fields': (
                                'first_name', 'last_name', 'email', 'phone_number',
                                'address', 'is_staff', 'is_active', 'is_superuser', 'is_farmer',
                                'password1', 'password2'
                        ),
                }),
        )
admin.site.register(NewUser, UserAdminConfig)
