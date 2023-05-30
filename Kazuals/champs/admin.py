from django.contrib import admin

from champs.models import Build


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}