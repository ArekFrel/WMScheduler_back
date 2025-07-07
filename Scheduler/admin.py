from django.contrib import admin
from .models import *

LIST_DISPLAY = (
    'Day',
    'first_shift_worker',
    'first_shift_time',
    'second_shift_worker',
    'second_shift_time')

@admin.register(F1Man)
class F1ManAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY

@admin.register(F3Dmg104)
class F3Dmg104Admin(admin.ModelAdmin):
    list_display = LIST_DISPLAY

@admin.register(F4Dmg144)
class F4Dmg144Admin(admin.ModelAdmin):
    list_display = LIST_DISPLAY

@admin.register(F5Vtc200)
class F5Vtc200dmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY

@admin.register(F6Vtc300)
class F6Vtc300dmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY

@admin.register(F7Cheto)
class AF7Chetodmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY

@admin.register(T1Man)
class T1Mandmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY

@admin.register(T2Man)
class T2ManAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY

@admin.register(T4Fct)
class T4FctAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY

@admin.register(T5Okuma)
class T5OkumaAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY

@admin.register(T6Integrex)
class T6IntegrexAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY

@admin.register(Pily)
class PilyAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY




