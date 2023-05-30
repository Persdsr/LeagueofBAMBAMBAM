from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from oauth.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'bio',
                    'gender',
                    'avatar',
                )
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'bio',
                    'gender',
                    'avatar',
                )
            }
        )
    )
