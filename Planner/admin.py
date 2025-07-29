from django.contrib import admin
from .models import *

@admin.register(ItemsToPlan)
class ItemsToPlanAdmin(admin.ModelAdmin):
    list_display = ('drawn_and_po', 'po', 'material')

    @staticmethod
    def drawn_and_po(obj):
        return f'{obj.po}__{obj.drawing}'

@admin.register(PilyPlanner)
class PilyPlannerAdmin(admin.ModelAdmin):
    pass
