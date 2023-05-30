from django.contrib import admin

from service.models import Meme


@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    pass
