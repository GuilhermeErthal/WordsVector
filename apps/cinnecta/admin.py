from django.contrib import admin

from .models import Texts


@admin.register(Texts)
class TextsAdmin(admin.ModelAdmin):
    list_display = ('text')