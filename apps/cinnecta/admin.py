from django.contrib import admin

from .models import Texts


@admin.register(Texts)
class TextsAdmin(admin.ModelAdmin):
    fields = ('text',)