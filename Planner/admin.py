from django.contrib import admin
from .models import *

@admin.register(ItemsToPlan)
class ItemsToPlanAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'drawing')

    @staticmethod
    def drawn_and_po(obj):
        return f'{obj.drawing}__{obj.po}'

@admin.register(PilyPlanner)
class PilyPlannerAdmin(admin.ModelAdmin):
    pass
